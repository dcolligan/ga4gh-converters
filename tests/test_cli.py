"""
Tests the cli
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest

import ga4gh.converters.cli.ga2vcf as cli_ga2vcf
import ga4gh.converters.cli.ga2sam as cli_ga2sam


class TestGa2VcfArguments(unittest.TestCase):
    """
    Tests the ga2vcf cli can parse all arguments it is supposed to
    """
    def testParseArguments(self):
        cliInput = """--key KEY -O vcf --outputFile /dev/null
        --referenceName REFERENCENAME --callSetIds CALL,SET,IDS --start 0
        --end 1 --pageSize 2 BASEURL VARIANTSETID"""
        parser = cli_ga2vcf.getGa2VcfParser()
        args = parser.parse_args(cliInput.split())
        self.assertEqual(args.key, "KEY")
        self.assertEqual(args.outputFormat, "vcf")
        self.assertEqual(args.outputFile, "/dev/null")
        self.assertEqual(args.referenceName, "REFERENCENAME")
        self.assertEqual(args.callSetIds, "CALL,SET,IDS")
        self.assertEqual(args.start, 0)
        self.assertEqual(args.end, 1)
        self.assertEqual(args.pageSize, 2)
        self.assertEquals(args.baseUrl, "BASEURL")
        self.assertEquals(args.variantSetId, "VARIANTSETID")


class TestGa2SamArguments(unittest.TestCase):
    """
    Tests the ga2sam cli can parse all arguments it is supposed to
    """
    def testParseArguments(self):
        cliInput = """--key KEY --outputFormat sam
        --pageSize 1 --start 2 --end 3 --outputFile OUT.SAM
        --referenceId REFERENCEID BASEURL READGROUPIDS"""
        parser = cli_ga2sam.getGa2SamParser()
        args = parser.parse_args(cliInput.split())
        self.assertEqual(args.key, "KEY")
        self.assertEqual(args.outputFormat, "sam")
        self.assertEqual(args.outputFile, "OUT.SAM")
        self.assertEqual(args.referenceId, "REFERENCEID")
        self.assertEqual(args.start, 2)
        self.assertEqual(args.end, 3)
        self.assertEqual(args.pageSize, 1)
        self.assertEquals(args.baseUrl, "BASEURL")
        self.assertEquals(args.readGroupIds, "READGROUPIDS")
