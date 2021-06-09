#!/usr/bin/python
#
# Copyright 2015 Google Inc. All Rights Reserved.

import inspect
import json
import optparse
import os
import sys

USAGE = """%prog src_path dst_path
Generate analytics enums for use in Javascript.

src_path    Path to the source code root directory.
dst_path    Path to store the 'enums.js' file."""


def main():
  parser = optparse.OptionParser(USAGE)
  _, args = parser.parse_args()

  if len(args) != 2:
    parser.error('Error: 2 arguments required.')

  src_path, dst_path = args[0:2]
  json_path = os.path.join(src_path, 'app_engine', 'bigquery')


  print(src_path, '>>>', dst_path)
  outfile = os.path.join(dst_path, 'enums.js')
  with open(outfile, 'w') as fp:
    fp.write("/* file generated by gen_js_enums.py */\n")
    fp.write("'use strict';\n")
    fp.write("\n")

    fp.write("var enums = ")
    fp.write(json.dumps(
        json.load(open(os.path.join(json_path, 'enums.json'))),
        indent=2))
    fp.write(";\n")


if __name__ == '__main__':
  main()
