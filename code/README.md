# Tools for SysML Data Conversion

These scripts were developed to facilitate data transformation (CVE or CWE data formats) into a format compatible with SysML modeling tools (CSV).

> Note: This thesis work focuses on CATIA | Magic Systems of Systems Architect 2024x
> and may not be compatible with other SysML tools without modification.

## json2csv.py

A Python script to convert JSON files (including multi-object or newline-delimited formats) into CSV format.

### Usage

```bash
python3 json2csv.py input.json output.csv
```

### Requirements

- Python 3.x
- json module (standard library)
- sys module (standard library)
- pandas module (install via `pip install pandas`)

## cwe-xml2msosa-csv.py

A Python script to convert CWE XML data into a CSV format compatible with Magic Systems of Systems Architect.

### Usage

```bash
python3 cwe-xml2msosa-csv.py [-h] -f FILE
```

### Requirements
- Python 3.x
- argparse module (standard library)
- xml.etree.ElementTree module (standard library)
- csv module (standard library)
- requests module (install via `pip install requests`)

# Tools for Updating Cybersecurity Vulnerability Management System (CVMS) Profile

## CVE Search

The [cve-search](https://github.com/cve-search/cve-search) project was used in this thesis to facilitate CVE data retrieval and management. 

### Notes 

"The main objective of the software is to avoid doing direct and public lookups into the public CVE databases. Local lookups are usually faster and you can limit your sensitive queries via the Internet.

cve-search includes a back-end to store vulnerabilities and related information, an intuitive web interface for search and managing vulnerabilities, a series of tools to query the system and a web API interface"