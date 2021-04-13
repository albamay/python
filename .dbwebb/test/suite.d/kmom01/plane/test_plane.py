#!/usr/bin/env python3
"""
Contains testcases for the individual examination.
"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
import sys
from unittest import TextTestRunner
from exam_test_case import ExamTestCase
from exam_test_result import ExamTestResult
from helper_functions import import_module
from helper_functions import find_path_to_assignment


FILE_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_PATH = find_path_to_assignment(FILE_DIR)


if REPO_PATH not in sys.path:
    sys.path.insert(0, REPO_PATH)

# Path to file and basename of the file to import
# plane = import_module(REPO_PATH, "plane") # Has inputs, use in check_print 



class Test1Plane(ExamTestCase):
    """
    Each assignment has 1 testcase with multiple asserts.
    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """
    HIGH_VALS = {
        "speed": {"input": "2100", "correct": "6889.76"},
        "height": {"input": "1020", "correct": "633.8"},
        "temp": {"input": "2192.0", "correct": "3977.6"}
    }
    LOW_VALS = {
        "speed": {"input": "23.23", "correct": "76.21"},
        "height": {"input": "65.0", "correct": "40.39"},
        "temp": {"input": "135.205", "correct": "275.37"}
    }
    NEGATIVE_VALS = {
        "speed": {"input": "-2.5", "correct": "-8.2"},
        "height": {"input": "-123.14", "correct": "-76.52"},
        "temp": {"input": "-252.454", "correct": "-422.42"}
    }

    @classmethod
    def setUpClass(cls):
        """
        To find all relative files that are read or written to.
        """
        os.chdir(REPO_PATH)

    def check_print_contain(self, inp, correct):
        """
        One function for testing print input functions
        """
        with patch('builtins.input', side_effect=inp):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                import_module(REPO_PATH, "plane")
                str_data = fake_out.getvalue()
                self.assertIn(correct, str_data)

    def test_a_speed_low_value(self):
        """
        Testar kilometer till miles
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.tags = ["speed"]
        self.norepr = True
        self._argument = [self.LOW_VALS["speed"]["input"]] * 3
        self.check_print_contain(self._argument, self.LOW_VALS["speed"]["correct"])
    
    def test_b_speed_high_values(self):
        """
        Testar kilometer till miles
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.tags = ["speed"]
        self.norepr = True
        self._argument = [self.HIGH_VALS["speed"]["input"]] * 3
        self.check_print_contain(self._argument, self.HIGH_VALS["speed"]["correct"])


    def test_c_speed_negative_values(self):
        """
        Testar kilometer till miles
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.tags = ["speed"]
        self.norepr = True
        self._argument = [self.NEGATIVE_VALS["speed"]["input"]] * 3
        self.check_print_contain(self._argument, self.NEGATIVE_VALS["speed"]["correct"])


    def test_d_height_low_value(self):
        """
        Testar meter till feet
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.tags = ["height"]
        self.norepr = True
        self._argument = [self.LOW_VALS["height"]["input"]] * 3
        self.check_print_contain(self._argument, self.LOW_VALS["height"]["correct"])
    
    def test_e_height_high_values(self):
        """
        Testar meter till feet
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.tags = ["height"]
        self.norepr = True
        self._argument = [self.HIGH_VALS["height"]["input"]] * 3
        self.check_print_contain(self._argument, self.HIGH_VALS["height"]["correct"])

    def test_f_height_negative_values(self):
        """
        Testar meter till feet
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.tags = ["height"]
        self.norepr = True
        self._argument = [self.NEGATIVE_VALS["height"]["input"]] * 3
        self.check_print_contain(self._argument, self.NEGATIVE_VALS["height"]["correct"])


    
    def test_g_temp_low_value(self):
        """
        Testar celcius till fahrenheit
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.tags = ["temp"]
        self.norepr = True
        self._argument = [self.LOW_VALS["temp"]["input"]] * 3
        self.check_print_contain(self._argument, self.LOW_VALS["temp"]["correct"])
    
    def test_h_temp_high_values(self):
        """
        Testar celcius till fahrenheit
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.tags = ["temp"]
        self.norepr = True
        self._argument = [self.HIGH_VALS["temp"]["input"]] * 3
        self.check_print_contain(self._argument, self.HIGH_VALS["temp"]["correct"])

    def test_i_temp_negative_values(self):
        """
        Testar celcius till fahrenheit
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.tags = ["temp"]
        self.norepr = True
        self._argument = [self.NEGATIVE_VALS["temp"]["input"]] * 3
        self.check_print_contain(self._argument, self.NEGATIVE_VALS["temp"]["correct"])

if __name__ == '__main__':
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)