#!/usr/bin/env python3

import hashlib
import json
import os
import sys
import re
import path_validation

stdin_contents = ""
for line in sys.stdin:
    stdin_contents += line

whitespace_regex_pattern = re.compile(r'\s+')
files_list = [filePath for filePath in re.sub(whitespace_regex_pattern, '', stdin_contents).split(',') if path_validation.is_pathname_valid(filePath)]

print(files_list)
print("DONE")