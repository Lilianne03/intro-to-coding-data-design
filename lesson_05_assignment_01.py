cities = {}
while True:
    city = input ("Please enter the name of a city: ")
    if city.lower() == "exit":
        break
    unit = input("Would you like to enter the temperature in Celsius or Farenheit?: ").lower()
    if unit == "farenheit":
        farenheit = float(input(f"Please enter the current temperature in Farenheit in {city}: "))
        celsius = (farenheit - 32)*5/9
    else:
        celsius = float(input(f"Please enter the current temperature in Celsius in {city}: "))
        farenheit = (celsius*9/5)+32
    raining = input(f"Is it raining in {city}? (yes/no):").lower()
    sunny = input(f"Is the sun shining in {city}? (yes/no):").lower()

    cities[city] = {"celsius" : celsius, "farenheit" : farenheit, "raining" : raining, "sunny" : sunny}

print("Summary")
for city, weather in cities.items():
    celsius = weather["celsius"]
    farenheit = weather["farenheit"]
    if weather["sunny"] == "yes":
        sun_text = "sun"
    else:
        sun_text = "no sun"
    if weather["raining"] == "yes":
        rain_text = "rain"
    else:
        rain_text = "no rain"

    print(f"{city}: {celsius:.1f} degrees celsius, {farenheit:.1f} degrees farenheit, "
            f"{sun_text} and {rain_text}")
    if celsius < 0: 
        print(f"Warning: The teperature in {city} is below the freezing point.")
    if weather["raining"] == "yes" and weather["sunny"] == "yes":
        print(f"There is a rainbow in {city}.")


