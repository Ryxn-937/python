inventory=[]

def add_item(item):
    inventory.append(item)
    print(add_item)

def count_items(inventory):
    if len(inventory) == 0:
        return 0
    else:
        return 1 + count_items(inventory[1:])
    
show_item = lambda item: print(f"Item in Stock: {item}")


def main():
    add_item(dog food)
    add_item(cat toy)
    add_item(bird cage)
    add_item(fish tank)

    for item in inventory:
        show_item()
    
    count_items()
    
