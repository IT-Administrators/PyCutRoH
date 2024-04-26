"""Testing the module with the python internal unittest module."""

import unittest

from addimportdir import importdir,removedir

importdir()

import src.pycutroh as pycutroh

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

    def test_calc_separator_pos(self):
        self.assertEqual(pycutroh.calc_separator_pos(self.content," "),[0,4,7,9,23,len(self.content)])
        teststring1 = "19.10.2023"
        self.assertEqual(pycutroh.calc_separator_pos(teststring1,"."),[0,2,5,len(teststring1)])

    def test_calc_fields(self):
        self.assertEqual(pycutroh.calc_fields((0,3),[0,4,7,9,23,len(self.content)]),[(0,4),(9,14)])
        teststring1 = "19.10.2023"
        self.assertEqual(pycutroh.calc_fields((0,2),[0,2,5,len(teststring1)]),[(0,2),(5,len(teststring1) -5 )])

# Testing the main functions. 
class TestPycutrohMainFunctions(unittest.TestCase):
    def setUp(self):
        self.content = "This is a demonstration string."

    def test_get_letter_on_pos(self):
        self.assertEqual(pycutroh.get_letter_on_pos(self.content, 0), "T")

    def test_get_letters_from_pos_to_pos(self):
        self.assertEqual(pycutroh.get_letters_from_pos_to_pos(self.content, (0, 25)), self.content[0:25])
        self.assertEqual(pycutroh.get_letters_from_pos_to_pos(self.content, (0, 9)), self.content[0:9])
        self.assertEqual(pycutroh.get_letters_from_pos_to_pos(self.content, (0, 10)), self.content[0:10])
        self.assertEqual(pycutroh.get_letters_from_pos_to_pos(self.content, (0, 20)), self.content[0:20])

    def test_get_fields(self):
        self.assertEqual(pycutroh.get_fields(self.content, (0, 3), " "),"This demonstration")
        self.assertEqual(pycutroh.get_fields(self.content, (0, 3, 1, 2, 4), " "),"This demonstration is a string.")

    def test_get_fields_new_separator(self):
        self.assertEqual(pycutroh.get_fields_new_separator(self.content, (0, 3), " ", "|"),"This|demonstration")
        self.assertEqual(pycutroh.get_fields_new_separator(self.content,(0,3,1,2,4)," ","|"),"This|demonstration|is|a|string.")
        # Specifiying just one field is currently not supported. 
        # self.assertEqual(pycutroh.get_fields_new_separator(self.content,(0,)," ","|"),"This|")

if __name__ == '__main__':
    # Verbose unittests.
    unittest.main(verbosity=2)
    removedir()