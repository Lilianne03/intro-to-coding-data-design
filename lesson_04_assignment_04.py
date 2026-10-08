numbers = list(range(1,21))
even_numbers = []
for number in numbers:
    if (number % 2 == 0):
        even_numbers.append(number)
print(f"The even numbers between 1 and 20 are: {even_numbers}.") 