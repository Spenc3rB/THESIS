#!/usr/bin/env python3
"""
json_to_csv.py
Convert a JSON file (possibly multi-object or newline-delimited) into CSV.
Inspired by https://github.com/vinay20045/json-to-csv
Usage:
    python json_to_csv.py input.json output.csv
"""

import json
import pandas as pd
import sys

def iter_json_objects(s):
    """Yield each JSON object from a possibly concatenated stream."""
    decoder = json.JSONDecoder()
    idx = 0
    length = len(s)
    while idx < length:
        while idx < length and s[idx].isspace():
            idx += 1
        if idx >= length:
            break
        try:
            obj, end = decoder.raw_decode(s, idx)
            yield obj
            idx = end
        except json.JSONDecodeError:
            idx += 1  # advance if we fail

def convert_json_to_csv(input_path, output_path):
    encodings_to_try = ["utf-8", "utf-8-sig", "utf-16", "utf-16-le", "utf-16-be", "latin-1"]
    content = None

    for enc in encodings_to_try:
        try:
            with open(input_path, "r", encoding=enc) as f:
                content = f.read()
            break
        except Exception:
            continue

    if content is None:
        print("Could not read file with known encodings.")
        sys.exit(1)

    objs = list(iter_json_objects(content))
    if not objs:
        try:
            objs = [json.loads(line) for line in content.splitlines() if line.strip()]
        except Exception:
            pass

    if not objs:
        print("No JSON objects could be parsed from the file.")
        sys.exit(1)

    df = pd.json_normalize(objs) # god bless pandas
    df.to_csv(output_path, index=False)
    print(f"Converted {len(objs)} records to CSV: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python json_to_csv.py input.json output.csv")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    convert_json_to_csv(input_path, output_path)
