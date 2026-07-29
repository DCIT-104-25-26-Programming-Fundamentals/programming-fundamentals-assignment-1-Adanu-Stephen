def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)


def find_maximum(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def find_minimum(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest


# Main Program
n = int(input("How many numbers? "))

if n <= 0:
    print("Error: Number of values must be positive.")
else:
    numbers = []

    for i in range(n):
        value = int(input(f"Enter number {i + 1}: "))
        numbers.append(value)

    print("\nResults:")
    print("Sum:", calculate_sum(numbers))
    print("Average:", calculate_average(numbers))
    print("Maximum:", find_maximum(numbers))
    print("Minimum:", find_minimum(numbers))