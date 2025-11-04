try:
    item = input("Enter the name of a new item: ")
    with open("items.txt", "a+") as file:
        file.write(item + "\n")
    with open("items.txt", "r") as file:
        items = file.read()
    print("\n--- Full List of Items ---")
    print(items)
except Exception as e:
    print("An error occurred:", e)
