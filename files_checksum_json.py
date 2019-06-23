#!/usr/bin/env python3

import hashlib
import json
import os
import sys
import re
import path_validation

def md5sum(filename):
    hash = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(128 * hash.block_size), b""):
            hash.update(chunk)
    return hash.hexdigest()

def main():
    stdin_contents = ""
    for line in sys.stdin:
        stdin_contents += line

    whitespace_regex_pattern = re.compile(r'\s+')
    files_list = [filePath for filePath in re.sub(whitespace_regex_pattern, '', stdin_contents).split(',') if path_validation.is_pathname_valid(filePath)]

    checksums_dict = {}
    for i in range(0, len(files_list)):
        current_file_path = files_list[i]
        current_file_md5sum = md5sum(current_file_path)
        checksums_dict.update({current_file_path:current_file_md5sum})

    # Print results to stdout
    print(json.dumps(checksums_dict))

if __name__ == "__main__":
    main()