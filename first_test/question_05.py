def get_numbers():
    numbers = input("输入数字（用空格隔开）：")
    numbers = numbers.split()
    if not numbers:
        return []
    return [float(number) for number in numbers]

def find_maximum(numbers):
    maximum = numbers[0]
    if not numbers:
        return None
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

def main():
    numbers = get_numbers()
    maximum = find_maximum(numbers)
    print(maximum)

if __name__ == "__main__":
    main()
