try:
    title = input("Enter the book title: ")
    year = input("Enter the publication year: ")

    if not (title.replace(" ", "").isalpha()):
        raise ValueError("Error: Title should contain only alphabets and spaces.")

    if not (year.isdigit() and len(year) == 4 and (year.startswith("19") or year.startswith("20"))):
        raise ValueError("Error: Year must be a 4-digit number starting with '19' or '20'.")

    print(f"\nBook Added Successfully!\nTitle: {title}\nYear: {year}")

except ValueError as e:
    print(e)

finally:
    print("\nProcess completed.")
