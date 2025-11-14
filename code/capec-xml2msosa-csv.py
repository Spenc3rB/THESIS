import xml.etree.ElementTree as ET
import csv
import argparse

def normalize_text(elem):
    """Return all text (including nested tags) as a single line."""
    if elem is None:
        return ""
    txt = "".join(elem.itertext())
    return txt.replace("\r", "").replace("\n", " ").strip()

def main(ifile, ofile):
    tree = ET.parse(ifile)
    root = tree.getroot()

    if root.tag.startswith("{"):
        ns_uri = root.tag.split("}")[0][1:]
        print(f"Detected namespace URI: {ns_uri}")
        ns = {"ns": ns_uri}
        attack_pattern_path = ".//ns:Attack_Pattern"
        description_path = "ns:Description"
    else:
        print("No namespace detected")
        ns = {}
        attack_pattern_path = ".//Attack_Pattern"
        description_path = "Description"

    attack_patterns = root.findall(attack_pattern_path, ns)
    print(f"[INFO] Found {len(attack_patterns)} CAPEC attack patterns in XML")

    with open(ofile, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            "CAPEC_ID",
            "Name",
            "Description",
            "URL"
        ])

        for ap in attack_patterns:
            capec_id = (ap.get("ID") or "").strip()
            name = (ap.get("Name") or "").strip()

            desc_elem = ap.find(description_path, ns)
            description = normalize_text(desc_elem)
            url = f"https://capec.mitre.org/data/definitions/{capec_id}.html"

            writer.writerow([capec_id, name, description, url])

    print(f"CAPEC CSV written to {ofile}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Parse CAPEC XML and output patterns to CSV."
    )
    parser.add_argument("-xml", type=str, required=True, help="Path to CAPEC XML file")
    parser.add_argument(
        "-csv", type=str, default="capec_output.csv", help="Path to output CSV file"
    )
    args = parser.parse_args()
    main(args.xml, args.csv)
