temp_value = input("Enter the temperature to convert: ")
temp_CF = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

if (temp_CF == "C" or temp_CF == "F") and isinstance(temp_value, int) :
        match temp_CF:
            case "C":
                def convert_to_fahrenheit(celsius):
                    global CELSIUS_TO_FAHRENHEIT_FACTOR
                    CELSIUS_TO_FAHRENHEIT_FACTOR = (CELSIUS_TO_FAHRENHEIT_FACTOR*celsius)+32
                    print(f"{celsius}°C is {CELSIUS_TO_FAHRENHEIT_FACTOR}°F")
                convert_to_fahrenheit(temp_value)
            case "F":
                def convert_to_celsius(fahrenheit):
                    global FAHRENHEIT_TO_CELSIUS_FACTOR
                    FAHRENHEIT_TO_CELSIUS_FACTOR = (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR
                    print(f"{fahrenheit}°F is {FAHRENHEIT_TO_CELSIUS_FACTOR}°C")
                convert_to_celsius(temp_value)
else:
    print("Invalid temperature. Please enter a numeric value.")

# git add . && git commit -m "function updata" && git push
# CELSIUS_TO_FAHRENHEIT_FACTOR\s*\+\s*32 
# CELSIUS_TO_FAHRENHEIT_FACTOR\s*\)\s*\+\s*32 - /tmp/correction/2465943663244944326984510408397459179239_5/100741/1508677/fns_and_dsa/temp_conversion_tool.py doesn't contain \(\s*CELSIUS_TO_FAHRENHEIT_FACTOR\s*\+\s*32\s*\) - /tmp/correction/2465943663244944326984510408397459179239_5/100741/1508677/fns_and_dsa/temp_conversion_tool.py doesn't contain 32\s*\+\s*\w+\s*\*\s*CELSIUS_TO_FAHRENHEIT_FACTOR