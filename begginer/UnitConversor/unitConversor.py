def celcius_for_fahrenheit(celcius):
    return (celcius * 9/5) + 32

def fahrenheit_for_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kilometers_for_miles(kilometers):
    return kilometers / 1.60934

def miles_for_kilometers(miles):
    return miles * 1.60934

def real_for_dollar(real, exchange_rate):
    return real / exchange_rate

def dollar_for_real(dollar, exchange_rate):
    return dollar * exchange_rate

while True:
    print("\nUnit Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kilometers to Miles")
    print("4. Miles to Kilometers")
    print("5. Brazilian Real to US Dollar")
    print("6. US Dollar to Brazilian Real")
    print("0. Exit")

    choice = input("Select an option (1-6): ")

    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        f = celcius_for_fahrenheit(c)
        print(f"{c}°C is {f:.2f}°F")

    elif choice == '2':
        f = float(input("Enter temperature in Fahrenheit: "))
        c = fahrenheit_for_celcius(f)
        print(f"{f}°F is {c:.2f}°C")

    elif choice == '3':
        km = float(input("Enter distance in Kilometers: "))
        miles = kilometers_for_miles(km)
        print(f"{km} km is {miles:.2f} miles")

    elif choice == '4':
        miles = float(input("Enter distance in Miles: "))
        km = miles_for_kilometers(miles)
        print(f"{miles} miles is {km:.2f} km")

    elif choice == '5':
        real = float(input("Enter amount in Brazilian Real: "))
        dollar = real_for_dollar(real, exchange_rate=5.0)
        print(f"R${real} is ${dollar:.2f}")

    elif choice == '6':
        dollar = float(input("Enter amount in US Dollar: "))
        real = dollar_for_real(dollar, exchange_rate=5.0)
        print(f"${dollar} is R${real:.2f}")

    elif choice == '0':
        print("Exiting Unit Converter.")
        break

    else:
        print("Invalid option. Please try again.")