#!/user/bin/env python3 -tt
"""
Counts strings in files. Example:
>>   ./diffstrings.py testfile1 testfile2 testfile3
<<   @testfile1
<<   string testfile1 only once
<<   string testfile1 twice



<<   @testfile1@testfile2
<<   string testfile1 testfile2 once



<<   @testfile2
<<   string testfile2 only once
<<   string testfile2 twice



<<   @testfile2@testfile3
<<   string testfile3 testfile2 once



<<   @testfile3
<<   string testfile3 only once
<<   string testfile3 twice


Copyrights (c) by Alexander Chikovany. Feel free to use or modify it if you need (but only if you like cats).
"""

import os
import sys
import getopt
import logging
from printer import Printer

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')
# logger.setLevel('CRITICAL')

def main(argv):

    files = []
    for f in argv:
        if not os.path.isfile(f):
            logger.warn("Did not found file: {filename}".format(filename=f))
        else:
            files.append(f)
    if len(files) < 2:
        logger.critical("Did not found enough files to make diff. Exiting")
        exit(1)
    makeDiff(files)

def makeDiff(files):
    """
    Show difference between all files listed at param

    Keyword arguments:
    files -- list of filepaths to make diff from
    """
    uniques = {}
    for f in files:
        uniques.update(_get_lines_count(f))
    files_am = len(files)
    strings_info = _count_all_lines(uniques)
    for string, am in strings_info.items():
        if am[0] > 0:
            _chop_same_lines(uniques, string, am[0])
    strings_info = _count_all_lines(uniques)
    p = Printer(files)
    for string, am in strings_info.items():
        p.add(_which_file_has_string(uniques, string), string)
    p.print()

def _chop_same_lines(uniques, string, am):
    """
    Delete all same strings from dataobject.

    Keyword arguments:
    uniques - dict of dicts of result of _get_lines_count function
    string - string, which repeats in files
    am - amount of minimal repeats string in every file

    Example:
    uniques  = {'file1': {'onestring': 1, 'everywherestring': 1}, 'file2': {'twostring': 1, 'everywherestring': 1}}
    uniques2 = {'file1': {'onestring': 1, 'everywherestring': 2}, 'file2': {'twostring': 1, 'everywherestring': 1}}

    _chop_same_lines(uniques, 'everywherestring', 1)  = {'file1': {'onestring': 1}, 'file2': {'twostring': 1}}
    _chop_same_lines(uniques2, 'everywherestring', 1) = {'file1': {'onestring': 1, 'everywherestring': 1}, 'file2': {'twostring': 1}}
    """
    for uniq in uniques.values():
        if uniq[string] == am:
            del uniq[string]
        else:
            uniq[string] -= am
    return uniques


def _which_file_has_string(uniques, string):
    result = []
    for filename, strings in uniques.items():
        if string in strings.keys():
            result.append(filename)
    return result

def _get_lines_count(filepath):
    """
    Returns dict contains amount of unique lines in file with filename as a key

    Keyword arguments:
    filepath -- filepath of file to make dict from
    """
    strings = {}
    with open(filepath, 'r') as f:
        for line in f:
            strings[line] = strings.get(line, 0) + 1
    return {filepath: strings}

def _count_all_lines(uniques):
    """
    Returns dict with information of min and max amount of string in files

    Keyword argumens:
    uniques -- dict contains amount of unique lines in files with filename as a key

    Example:
        uniques = {'file1': {'onestring': 1, 'everywherestring': 1}, 
                   'file2': {'twostring': 1, 'everywherestring': 1}}
        result = {'onestring': [0, 1], 'everywherestring': [1, 1], 'twostring': [0, 1]}
    """
    result = {}
    for strings_info in uniques.values():
        for string in strings_info.keys():
            result[string] = [ min(list(strs.get(string, 0) for strs in uniques.values())),
                             max(list(strs.get(string, 0) for strs in uniques.values()))]
    return result


if __name__ == '__main__':
    main(sys.argv[1:])
