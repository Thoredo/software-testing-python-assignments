getting_number = True

while getting_number:
    try:
        number = float(input("please input the cost of a product without VAT: "))
        getting_number = False
    except ValueError:
        print("Please give a proper number.")

vat = number * 1.21

print(f"The price with VAT is €{vat:.2f}")
