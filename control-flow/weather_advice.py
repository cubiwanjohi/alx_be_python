weather = input("What's the weather like today? (sunny/rainy/cold): ")
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Take an umbrella and wear waterproof shoes.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Weather type not recognized. Please enter sunny, rainy, or cold.")
