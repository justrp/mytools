#!/user/bin/env python3 -tt
"""
Counts strings in files. Example:
    ./diffstrings.py file otherfile anotherfile
    <some c00l output>

Copyrights (c) by Alexander Chikovany. Feel free to use or modify it if you need (but only if you like cats).
"""

import os
import sys
import getopt
import logging


def main(argv):
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.setLevel('DEBUG')
    # logger.setLevel('CRITICAL')

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
    pass


if __name__ == '__main__':
    main(sys.argv[1:])
