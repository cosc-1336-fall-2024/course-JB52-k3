#
import unittest
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget

class Test_Config(unittest.TestCase):
    
    def setUp(self):
        self.inventory = {}
    
    def test_add_inventory(self):
        add_inventory(self.inventory, "Widget1", 10)
        self.assertEqual(self.inventory["Widget1"], 10)
        
    
        add_inventory(self.inventory, "Widget1", 25)
        self.assertEqual(self.inventory["Widget1"], 35)
        
        add_inventory(self.inventory, "Widget1", -10)
        self.assertEqual(self.inventory["Widget1"], 25)

    def test_remove_inventory_widget(self):
        add_inventory(self.inventory, "Widget1", 10)
        add_inventory(self.inventory, "Widget2", 15)
        self.assertEqual(len(self.inventory), 2)
        
      
        remove_inventory_widget(self.inventory, "Widget1")
        
    
        self.assertNotIn("Widget1", self.inventory)
        self.assertIn("Widget2", self.inventory)
        self.assertEqual(len(self.inventory), 1)
