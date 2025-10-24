inventory = []

def add_item(item):
    inventory.append(item)

def main():
    add_item("dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")

main()

def count_items(items):
   if not items:
       return 0
   else:
       return 1 +  count_items(items[1:])
   
show_item = lambda item: print(f"Item in Stock: {item}")



for item in inventory:
    show_item(item)

total = count_items(inventory)
print(f"Total number of items in stock:",total)