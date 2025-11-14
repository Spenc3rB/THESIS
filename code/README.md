# Tools for SysML Data Conversion

These scripts were developed to facilitate data transformation (CVE or CWE data formats) into a format compatible with SysML modeling tools (CSV).

> Note: This thesis work focuses on CATIA | Magic Systems of Systems Architect 2024x
> and may not be compatible with other SysML tools without modification.

# Pre-requisites

- [Python 3.x](https://www.python.org/downloads/)
- Command Line Interface (CLI) access (e.g., Command Prompt, PowerShell, Terminal) and basic familiarity.

## json2csv.py

A Python script to convert JSON files (including multi-object or newline-delimited formats) into CSV format.

### Usage

```
python3 json2csv.py input.json output.csv
```

### Example

```
python3 .\json2csv.py .\sample-databases\esp8266.json .\sample-databases\esp8266.csv                        
Converted 4 records to CSV: .\sample-databases\esp8266.csv
```

## cwe-xml2msosa-csv.py

A Python script to convert CWE XML data into a CSV format compatible with Magic Systems of Systems Architect.

### Usage

```
python3 cwe-xml2msosa-csv.py -h
Current CWE API Metadata:
CWE Version: 4.18
Release Date: 2025-09-09
Total Weaknesses: 969
Total Categories: 410
Total Views: 56
usage: cwe-xml2msosa-csv.py [-h] -xml XML [-csv CSV]

Parse CWE XML and output to CSV. It's recommended to download the latest CWE XML from https://cwe.mitre.org/.

options:
  -h, --help  show this help message and exit
  -xml XML    Path to CWE XML file
  -csv CSV    Path to output CSV file
```

### Example

```
python3 .\cwe-xml2msosa-csv.py -xml .\sample-databases\cwec_v4.18.xml -csv .\sample-databases\cwec_v4.18.csv      
Current CWE API Metadata:
CWE Version: 4.18
Release Date: 2025-09-09
Total Weaknesses: 969
Total Categories: 410
Total Views: 56
Detected namespace URI: http://cwe.mitre.org/cwe-7
[INFO] Found 969 CWE weaknesses in XML
CWE CSV written to .\sample-databases\cwec_v4.18.csv
```

## capec-xml2msosa-csv.py

A Python script to convert CAPEC XML data into a CSV format compatible with Magic Systems of Systems Architect.

### Usage

```
python3 capec-xml2msosa-csv.py -h
usage: capec-xml2msosa-csv.py [-h] -xml XML [-csv CSV]

Parse CAPEC XML and output ID, Name, and Likelihood Of Attack to CSV. It's recommended to download the latest CAPEC XML from https://capec.mitre.org/

options:
  -h, --help  show this help message and exit
  -xml XML    Path to CAPEC XML file
  -csv CSV    Path to output CSV file
```

### Example

```
python3 .\capec-xml2msosa-csv.py -xml .\sample-databases\capec_latest.xml -csv .\sample-databases\capec_latest.csv
Detected namespace URI: http://capec.mitre.org/capec-3
[INFO] Found 615 CAPEC attack patterns in XML
CAPEC CSV written to .\sample-databases\capec_latest.csv
```

# Tools for Updating Cybersecurity Vulnerability Management System [(CVMS) Profile](../SysML/)

> Note: CVE search is used with the CVMS profile due to the constant updates in CVE data. CWEs and CAPECs are more static, so they can be updated less frequently.

## CVE Search

The [cve-search](https://github.com/cve-search/cve-search) project was used in this thesis to facilitate CVE data retrieval and management. 

### Notes from the developers:

"The main objective of the software is to avoid doing direct and public lookups into the public CVE databases. Local lookups are usually faster and you can limit your sensitive queries via the Internet.

cve-search includes a back-end to store vulnerabilities and related information, an intuitive web interface for search and managing vulnerabilities, a series of tools to query the system and a web API interface"