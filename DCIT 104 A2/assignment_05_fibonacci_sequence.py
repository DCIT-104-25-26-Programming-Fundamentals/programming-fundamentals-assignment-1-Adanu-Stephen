def print_fibonacci():
    try:
        n = int(input("How many terms? "))

        if n <= 0:
            print("Error: N must be a positive integer.")
            return

        a = 0
        b = 1

        print("Fibonacci sequence:", end=" ")

        for i in range(n):
            print(a, end=" ")
            c = a + b
            a = b
            b = c

        print()

    except ValueError:
        print("Error: N must be a positive integer.")


def check_fibonacci():
    try:
        num = int(input("Enter a number to check: "))

        if num < 0:
            print(f"{num} is NOT a Fibonacci number.")
            return

        a = 0
        b = 1

        while a < num:
            c = a + b
            a = b
            b = c

        if a == num:
            print(f"{num} is a Fibonacci number.")
        else:
            print(f"{num} is NOT a Fibonacci number.")

    except ValueError:
        print("Error: Please enter a valid integer.")


# Main program
print_fibonacci()
check_fibonacci()