import unittest

from src.examples.b_input_proc_output.input_process_output import float_division, integer_division, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_float_division(self):
        self.assertEqual(2.5, float_division(5,2))    

    def test_integer_division(self):
        self.assertEqual(2.5, integer_division(5,2))    

