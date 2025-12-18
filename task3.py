Flying Carpet...............$119.99
Phoenix Feather.............$14.99
Time Turner.................$84.99
Enchanted Sword.............$65.55
Posion of Luck..............$11.99
Crystal Ball................$39.99
""")

    # Shopkeeper's rule: All purchases must be at least 3 items for good luck!
    # (Don't worry - the shopkeeper checks every order himself)
    item = input("What item do you want?")
    price = float(input("This is the price of this item."))
    quantity = int(input("The max that you can get is 3."))

    # TODO: Calculate subtotal, tax, and total
    subtotal = quantity * price
    # Tax rate: 9.5%
    tax = subtotal * .095
    total = subtotal + tax

    # TODO: Round total to 2 decimal places using round()

    total = round(total,2)

    # TODO: Print receipt
    print("--------------------------")

    print(f"{item} x{quantity} @ ${price} each")

    print("--------------------------")
    # Print subtotal, tax, and total here
    print(f"Subtotal: ${subtotal}")
    print(f"Tax: ${tax}")
    print(f"Total: ${total}")


    print("\nThank you for shopping at\nthe Peculiar Emporium!")

    # The Peculiar Emporium


if __name__ == "__main__":
    main()
