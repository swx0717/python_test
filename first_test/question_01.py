numbers = [12, -3, 0, 7, 18, -5, 20, 11]
positive_number = []
negative_number = []
zero_number = []
for number in numbers:
    if number > 0:
        positive_number.append(number)
    elif number < 0:
        negative_number.append(number)
    else:
        zero_number.append(number)
print(len(positive_number))
print(len(negative_number))
print(len(zero_number))

even_number = []
odd_number = []
for number in numbers:
    if number % 2 == 0:
        even_number.append(number)
    else:
        odd_number.append(number)
print(len(even_number))
print(len(odd_number))