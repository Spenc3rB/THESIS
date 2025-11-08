import xml.etree.ElementTree as ET
import csv
import argparse
import requests

CWE_VERSION_API = "https://cwe-api.mitre.org/api/v1/cwe/version"

def normalize_text(elem):
    """Return all text (including nested tags) as a single line."""
    if elem is None:
        return ""
    txt = "".join(elem.itertext())
    return txt.replace("\r", "").replace("\n", " ").strip()

def fetch_cwe_api():
    try:
        r = requests.get(CWE_VERSION_API)
        r.raise_for_status()
        if r.headers.get("content-type", "").startswith("application/json"):
            data = r.json()
        else:
            data = {}
        version = data.get("ContentVersion", "")
        release_date = data.get("ContentDate", "")
        total_weaknesses = data.get("TotalWeaknesses", 0)
        total_categories = data.get("TotalCategories", 0)
        total_views = data.get("TotalViews", 0)
        return version, release_date, total_weaknesses, total_categories, total_views
    except Exception as e:
        print(f"[WARN] Could not fetch CWE API: {e}")
        return "", "", "", "", ""

def main(file, version):
    tree = ET.parse(file)
    root = tree.getroot()

    if root.tag.startswith("{"):
        ns_uri = root.tag.split("}")[0][1:]
        print(f"Detected namespace URI: {ns_uri}")
        ns = {"ns": ns_uri}
        weakness_path = ".//ns:Weakness"
        desc_path = ".//ns:Description"
        usage_path = ".//ns:Usage"
        if version != root.get("Version", ""):
            print(f"[WARN] CWE version mismatch: API version {version} vs XML version {root.get('Version', '')}")
            print("[WARN] Consider updating the CWE XML file.")
    else:
        print("No namespace detected")
        ns = {}
        weakness_path = ".//Weakness"
        desc_path = ".//Description"
        usage_path = ".//Usage"

    weaknesses = root.findall(weakness_path, ns)
    print(f"[INFO] Found {len(weaknesses)} CWE weaknesses in XML")

    with open("output.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["CWE_ID", "Name", "Description", "URL"])

        for w in weaknesses:
            usage_elem = w.find(usage_path, ns)
            usage = normalize_text(usage_elem)

            if usage not in ("Allowed", "Allowed-with-Review"):
                continue

            cwe_id = (w.get("ID") or "").strip()
            name = (w.get("Name") or "").strip()

            desc_elem = w.find(desc_path, ns)
            description = normalize_text(desc_elem)

            writer.writerow([cwe_id, name, description, f"https://cwe.mitre.org/data/definitions/{cwe_id}.html"])

    print("Filtered CSV written to output.csv")

if __name__ == "__main__":
    version, release_date, total_weaknesses, total_categories, total_views = fetch_cwe_api()
    print("Current CWE API Metadata:")
    print(f"CWE Version: {version}")
    print(f"Release Date: {release_date}")
    print(f"Total Weaknesses: {total_weaknesses}")
    print(f"Total Categories: {total_categories}")
    print(f"Total Views: {total_views}")
    parser = argparse.ArgumentParser(description="Parse CWE XML and output to CSV.")
    parser.add_argument("-f", "--file", required=True, help="Path to the CWE XML file")
    args = parser.parse_args()
    main(args.file, version)
