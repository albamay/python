#!/usr/bin/env python3
"""
An autogenerated testfile for python.
"""

import unittest
from io import StringIO
import os
import sys
from unittest.mock import patch
from unittest import TextTestRunner
from examiner import ExamTestCase, ExamTestResult, tags
from examiner import import_module, find_path_to_assignment


FILE_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_PATH = find_path_to_assignment(FILE_DIR)

if REPO_PATH not in sys.path:
    sys.path.insert(0, REPO_PATH)

# Path to file and basename of the file to import
backpack = import_module(REPO_PATH, 'inventory')
main = import_module(REPO_PATH, 'main')



class Test4ExtraInventory(ExamTestCase):
    """
    Each assignment has 1 testcase with multiple asserts.
    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """

    link_to_assignment = "https://dbwebb.se/uppgift/din-egen-chattbot-marvin-steg-3-v4#extra"

    @classmethod
    def setUpClass(cls):
        """
        To find all relative files that are read or written to.
        """
        os.chdir(REPO_PATH)



    def check_print_contain(self, inp, correct):
        """
        One function for testing print input functions.
        """
        with patch("builtins.input", side_effect=inp):
            with patch("sys.stdout", new=StringIO()) as fake_out:
                main.main()
                for val in correct:
                    str_data = fake_out.getvalue()
                    self.assertIn(val, str_data)



    def check_print_not_contain(self, inp, correct):
        """
        One function for testing print input functions.
        """
        with patch("builtins.input", side_effect=inp):
            with patch("sys.stdout", new=StringIO()) as fake_out:
                main.main()
                for val in correct:
                    str_data = fake_out.getvalue()
                    self.assertNotIn(val, str_data)



    @tags("inv", "range")
    def test_inventory_range_included(self):
        """
        Testar att anropa "inventory" funktionen, med värde för sekvens utskrift.
        Kollar att rätt värden är med i utskriften.
        Använder följande som argument:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments  = [["java", "c#", "python", "js", "c++"], 1, 4]


        with patch("sys.stdout", new=StringIO()) as fake_out:
            backpack.inventory(*self._multi_arguments)
            str_data = fake_out.getvalue()

        for val in self._multi_arguments[0][1:4]:
            self.assertIn(val, str_data)



    @tags("inv", "range")
    def test_inventory_range_excluded(self):
        """
        Testar att anropa "inventory" funktionen, med värde för sekvens utskrift.
        Kollar att rätt värden saknas från utskriften.
        Använder följande som argument:
        {arguments}
        Förväntar att följande inte finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments  = [["java", "c#", "python", "js", "php"], 1, 4]


        with patch("sys.stdout", new=StringIO()) as fake_out:
            backpack.inventory(*self._multi_arguments)
            str_data = fake_out.getvalue()

        for val in ["java", "php"]:
            self.assertNotIn(val, str_data)



    @tags("inv", "range")
    def test_inventory_range__meny_negative_included(self):
        """
        Testar att anropa "inv" menyval, med negativt värde för sekvens utskrift.
        Kollar att rätt värden är med i utskriften.
        Använder följande som argument:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments  = [["monkey", "doggo", "catty cat"], -3, -1]


        with patch("sys.stdout", new=StringIO()) as fake_out:
            backpack.inventory(*self._multi_arguments)
            str_data = fake_out.getvalue()

        for val in self._multi_arguments[0][-3:-1]:
            self.assertIn(val, str_data)



    @tags("inv", "range")
    def test_inventory_range__meny_negative_excluded(self):
        """
        Testar att anropa "inv" menyval, med negativt värde för sekvens utskrift.
        Kollar att rätt värden saknas från utskriften.
        Använder följande som argument:
        {arguments}
        Förväntar att följande inte finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments  = [["monkey", "doggo", "catty cat"], -3, -1]

        with patch("sys.stdout", new=StringIO()) as fake_out:
            backpack.inventory(*self._multi_arguments)
            str_data = fake_out.getvalue()

        for val in ["catty cat"]:
            self.assertNotIn(val, str_data)



if __name__ == '__main__':
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
