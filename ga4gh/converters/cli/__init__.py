"""
Shared cli methods
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


def addOutputFileArgument(parser):
    parser.add_argument(
        "--outputFile", "-o", default=None,
        help="the file to write the output to")
