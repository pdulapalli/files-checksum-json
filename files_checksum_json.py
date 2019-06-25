#!/usr/bin/env python3

import hashlib
import json
import os
import sys
import re
import path_validation

DEFAULT_BLOCK_SIZE = 65536 # 64kb chunks

def sha256sum(fname, blocksize):
    hash = hashlib.sha256()
    with open(fname, 'rb') as f:
        while True:
            block = f.read(blocksize)
            if not block:
                break
            hash.update(block)

    return hash.hexdigest()

def main():
    stdin_contents = ""
    for line in sys.stdin:
        stdin_contents += str(line)

    whitespace_regex_pattern = re.compile(r'\s+')
    files_list = [filePath for filePath in re.sub(whitespace_regex_pattern, '', stdin_contents).split(',') if path_validation.is_pathname_valid(filePath)]

    checksums_dict = {}
    for i in range(0, len(files_list)):
        current_file_path = files_list[i]

        if os.path.exists(current_file_path):
            current_file_sha256sum = sha256sum(current_file_path, DEFAULT_BLOCK_SIZE)
            checksums_dict[current_file_path] = current_file_sha256sum
        else:
            checksums_dict[current_file_path] = None

    # Print results to stdout
    print(json.dumps(checksums_dict))

if __name__ == "__main__":
    main()