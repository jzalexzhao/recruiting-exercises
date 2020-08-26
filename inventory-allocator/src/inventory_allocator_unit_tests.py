import unittest
from inventory_allocator import InventoryAllocator

class InventoryAllocatorTests(unittest.TestCase):

    def test_happy(self):
        inventory_allocator = InventoryAllocator()

        order = { 'apple': 1 }
        inventory_distribution  = [{ 'name': 'owd',  'inventory': { 'apple': 1 } }]
        expected_output = [{ 'owd': { 'apple': 1 } }]
        
        self.assertEqual(inventory_allocator.best_shipment(order, inventory_distribution), expected_output)

    def test_fully_not_enough(self):
        inventory_allocator = InventoryAllocator()

        order = { 'apple': 1 }
        inventory_distribution  = [{ 'name': 'owd',  'inventory': { 'apple': 0 } }]
        expected_output = []
        
        self.assertEqual(inventory_allocator.best_shipment(order, inventory_distribution), expected_output)

    def test_partially_not_enough(self):
        inventory_allocator = InventoryAllocator()

        order = { 'apple': 1, 'banana': 3 }
        inventory_distribution  = [
            { 'name': 'owd',  'inventory': { 'apple': 1, 'banana': 2 } },
            { 'name': 'dm', 'inventory': { 'apple': 5 }}]

        expected_output = []
        
        self.assertEqual(inventory_allocator.best_shipment(order, inventory_distribution), expected_output)

    def test_split_items(self):
        inventory_allocator = InventoryAllocator()

        order = { 'apple': 10 }
        inventory_distribution  = [
            { 'name': 'owd',  'inventory': { 'apple': 5 } },
            { 'name': 'dm',  'inventory': { 'apple': 5 } }
            ]
        expected_output = [{ 'owd': { 'apple': 5 } }, { 'dm': { 'apple': 5 } }]
        
        self.assertEqual(inventory_allocator.best_shipment(order, inventory_distribution), expected_output)

    def test_more_than_enough_inventory(self):
        inventory_allocator = InventoryAllocator()

        order = { 'apple': 10, 'pear': 20 }
        inventory_distribution  = [
            { 'name': 'abc',  'inventory': { 'apple': 100 } },
            { 'name': 'def',  'inventory': { 'apple': 200, 'pear': 1000 } }
            ]
        expected_output = [{ 'abc': { 'apple': 10 } }, { 'def': { 'pear': 20 } }]
        
        self.assertEqual(inventory_allocator.best_shipment(order, inventory_distribution), expected_output)
    
    def test_empty_inventory(self):
        inventory_allocator = InventoryAllocator()

        order = { 'apple': 10 }
        inventory_distribution  = []
        expected_output = []
        
        self.assertEqual(inventory_allocator.best_shipment(order, inventory_distribution), expected_output)

    def test_empty_order(self):
        inventory_allocator = InventoryAllocator()

        order = {}
        inventory_distribution  = [
            { 'name': 'owd',  'inventory': { 'apple': 5 } },
            { 'name': 'dm',  'inventory': { 'apple': 5 } }
            ]
        expected_output = []

        self.assertEqual(inventory_allocator.best_shipment(order, inventory_distribution), expected_output)
    
    def test_empty_order_inventory(self):
        inventory_allocator = InventoryAllocator()

        order = {}
        inventory_distribution  = []
        expected_output = []

        self.assertEqual(inventory_allocator.best_shipment(order, inventory_distribution), expected_output)
    
    def test_zero_orders(self):
        inventory_allocator = InventoryAllocator()

        order = { 'apple': 0, 'pear': 0 }
        inventory_distribution  = [
            { 'name': 'owd',  'inventory': { 'apple': 5 } },
            { 'name': 'dm',  'inventory': { 'pear': 5 } }
            ]
        expected_output = []

        self.assertEqual(inventory_allocator.best_shipment(order, inventory_distribution), expected_output)

    def test_zero_order_inventory(self):
        inventory_allocator = InventoryAllocator()

        order = { 'apple': 0, 'pear': 0 }
        inventory_distribution  = [
            { 'name': 'owd',  'inventory': { 'apple': 0 } },
            { 'name': 'dm',  'inventory': { 'pear': 0 } }
            ]
        expected_output = []

        self.assertEqual(inventory_allocator.best_shipment(order, inventory_distribution), expected_output)


if __name__ == '__main__':
    unittest.main()