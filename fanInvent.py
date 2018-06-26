def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for dkey, dval in inventory.items():
        print(str(dval) + " " + dkey)
        item_total += dval
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory.keys():
            oldVal = inventory.get(item)
            inventory[item] = oldVal + 1
        else:
            inventory[item] = 1
    return inventory


myStuff = {'Gold Coin': 42, 'Rope': 1}
dragonLoot = ['Gold Coin', 'Dagger', 'Gold Coin', 'Gold Coin', 'Ruby']

myStuff = addToInventory(myStuff,dragonLoot)

displayInventory(myStuff)