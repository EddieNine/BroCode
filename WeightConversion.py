weight = float(input("Enter your Weight: "))
unit = input("Kilograms or Pounds? (K or L): ").strip().upper()

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f'Your weight is: {weight:.2f} {unit}')
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f'Your weight is: {weight:.2f} {unit}')
else:
    print(f'{unit} was not valid')