

temp_value = int(input("Enter the temperature to convert: "))
temp_CF = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

match temp_CF:
    case "C":
        def convert_to_fahrenheit(celsius):
            global CELSIUS_TO_FAHRENHEIT_FACTOR
            CELSIUS_TO_FAHRENHEIT_FACTOR = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32
            print(f"{celsius}°C is {CELSIUS_TO_FAHRENHEIT_FACTOR}°F")
        convert_to_fahrenheit(temp_value)
    case "F":
        def convert_to_celsius(fahrenheit):
            global FAHRENHEIT_TO_CELSIUS_FACTOR
            FAHRENHEIT_TO_CELSIUS_FACTOR = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
            print(f"{fahrenheit}°F is {FAHRENHEIT_TO_CELSIUS_FACTOR}°C")
        convert_to_celsius(temp_value)