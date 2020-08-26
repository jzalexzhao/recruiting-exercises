from typing import List
from copy import deepcopy

# constants for string literals
NAME = 'name'
INVENTORY = 'inventory'

class InventoryAllocator:

    def best_shipment(self, order:dict, inventory_distribution: List[dict]):
        """
        Computes the best way an order can be shipped given inventory across a set of warehouses

        Args:
            order (dict): items that are being ordered and sorted in terms of the cost
            inventory_distribution (List[dict]): list of objects with warehouse name and inventory amounts

        Returns:
            List(dict): the cheapest shipment 
        """

        shipments = []
        # make copies of the inputs, since we want to mutate them in the code
        order_cp = deepcopy(order)

        
        for warehouse in inventory_distribution:
            # check if we still need more orders
            if len(order_cp) == 0:
                break
        
            warehouse_name = warehouse[NAME]
            warehouse_inventory = warehouse[INVENTORY]
            curr_shipment = {} # potential fullfilled order from the ware house
            curr_shipment[warehouse_name] = {}
            curr_inventory = curr_shipment[warehouse_name]

            for item,amount in warehouse_inventory.items():
                # check if the item is needed by the order
                if item in order_cp and order_cp[item] > 0 and amount > 0:
                    item_needed = order_cp[item]
                    order_cp[item] = max(0, item_needed - amount)
                    curr_inventory[item] = min(item_needed, amount)
                    
                    # if the order is fullfilled, then delete it
                    if order_cp[item] == 0:
                        del order_cp[item]
                    
            # put the shipment in the answer if there is any
            if len(curr_shipment) > 0:
                shipments.append(curr_shipment)

        # check if all orders are fullfilled
        if len(order_cp) == 0:
            return shipments
        else:
            return []
