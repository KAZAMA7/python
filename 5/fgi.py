#!/usr/bin/python3
## Fancy game inventory progtramme
import pprint

inventory = {'rope': 6, 'arrows': 10, 'Bow': 1, 'guns': 7, 'Bullets': 1000, 'tractor': 1, 'axe': 2}

def displayInventory(inv):
  print('inventory:')
  total_inv = 0
  for k, v in inv.items():
   print(str(v) + ' ' + k)
   total_inv = v + total_inv
  print('The total number of items in the inventory are ' + str(total_inv))
displayInventory(inventory)
