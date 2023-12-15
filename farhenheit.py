def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    try:
        choice = int(input("Enter your choice (1 or 2): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if choice == 1:
        try:
            celsius_temperature = float(input("Enter temperature in Celsius: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        result_fahrenheit = celsius_to_fahrenheit(celsius_temperature)
        print(f"{celsius_temperature}°C is equal to {result_fahrenheit}°F")
    elif choice == 2:
        try:
            fahrenheit_temperature = float(input("Enter temperature in Fahrenheit: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        result_celsius = fahrenheit_to_celsius(fahrenheit_temperature)
        print(f"{fahrenheit_temperature}°F is equal to {result_celsius}°C")
    else:
        print("Invalid choice. Please enter either 1 or 2.")

if __name__ == "__main__":
    main()
