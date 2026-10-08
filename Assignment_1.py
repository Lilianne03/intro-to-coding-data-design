# Ask the user for the city name
# Ask the user for the current temperature in Celsius
# Convert the temperature to float
# Print the user input in a formatted string
city = input("Enter the name of your city") 
temperature = float(input(f"Enter the current temperature in {city} in degree Celsius"))
print(f"The current temperature in {city} is {temperature} degrees celcius.")

# Ask the user for the city names
# Ask the user for the current temperatures in Celsius
# Convert the temperatures to float
# Calculate the average temperature
# Print the user input in a formatted string
city_1 = input("Enter the name of your first destination city")
city_2 = input("Enter the name of your second destination city")
temperature_1 = float(input(f"Enter the current temperature in {city_1} in degree Celsius"))
temperature_2 = float(input(f"Enter the current temperature in {city_2} in degree Celsius"))
average = (temperature_1+temperature_2)/2
print(f"The average temperature in {city_1} and {city_2} is {average} degrees celcius.")

# Ask the user for the city names
# Ask the user for the current temperatures in Celsius
# Convert the temperatures to float
# Calculate the average temperature
# Print the user input in a formatted string
# Convert the average temperature to Fahrenheit
city_1 = input("Enter the name of your first destination city")
city_2 = input("Enter the name of your second destination city")
temperature_1 = float(input(f"Enter the current temperature in {city_1} in degree Celsius"))
temperature_2 = float(input(f"Enter the current temperature in {city_2} in degree Celsius"))
average = (temperature_1+temperature_2)/2
print(f"The average temperature in {city_1} and {city_2} is {average} degrees celcius.")
temperature_f = float(average*9/5)+32
print(f"That's {temperature_f} degrees farenheit.")