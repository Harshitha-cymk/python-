print("UNIT CONVERTER")
print("1. Kilometre to Metre")
print("2. Metre to Kilometre")
print("3. Metre to Centimetre")
print("4. Centimetre to Metre")

choice = int(input("Enter your choice: "))
value = float(input("Enter value: "))

if choice == 1:
    print("Result =", value * 1000, "metres")
elif choice == 2:
    print("Result =", value / 1000, "kilometres")
elif choice == 3:
    print("Result =", value * 100, "centimetres")
elif choice == 4:
    print("Result =", value / 100, "metres")
else:
    print("Invalid choice")
