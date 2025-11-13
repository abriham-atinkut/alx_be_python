# Prompt the user for weather input
weather_user = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Provide clothing recommendations based on the input
if weather_user == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_user == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather_user == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
