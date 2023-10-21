"""Testing the module with the python internal unittest module."""

import unittest
import pycutroh

# Testing helper functions
class TestPycutrohHelperFunctions(unittest.TestCase):
    def setUp(self):
        self.content = "This is a demonstration string."

    def test_pos_handling(self):
        self.assertEqual(pycutroh.pos_handling(1), 0)
        self.assertEqual(pycutroh.pos_handling(0), 0)
        self.assertEqual(pycutroh.pos_handling(2), 1)
    
    def test_remove_leading_separator(self):
        self.assertEqual(pycutroh.remove_leading_separator(self.content, self.content[0]), self.content[1:])

    def test_replace_separator(self):
        self.assertEqual(pycutroh.replace_separator(self.content, " ", "|"), self.content.replace(" ", "|"))

# Testing the main functions. 
class TestPycutrohMainFunctions(unittest.TestCase):
    def setUp(self):
        self.content = "This is a demonstration string."

    def test_get_letter_on_pos(self):
        self.assertEqual(pycutroh.get_letter_on_pos(self.content, 0), "T")

    def test_get_letters_from_pos_to_pos(self):
        self.assertEqual(pycutroh.get_letters_from_pos_to_pos(self.content, (0, 25)), self.content[0:25])

    def test_get_fields(self):
        self.assertEqual(pycutroh.get_fields(self.content, (0, 3), " "),"This demonstration")
        self.assertEqual(pycutroh.get_fields(self.content, (0, 3, 1, 2, 4), " "),"This demonstration is a string.")

    def test_get_fields_new_separator(self):
        self.assertEqual(pycutroh.get_fields_new_separator(self.content, (0, 3), " ", "|"),"This|demonstration")
        self.assertEqual(pycutroh.get_fields_new_separator(self.content,(0,3,1,2,4)," ","|"),"This|demonstration|is|a|string.")

if __name__ == '__main__':
    # Verbose unittests.
    unittest.main(verbosity=2)