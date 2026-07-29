def single_table():
    try:
        number = int(input("Enter a number: "))

        if number <= 0:
            print("Error: Number must be a positive integer.")
            return

        print(f"\nMultiplication Table for {number}:")

        for i in range(1, 13):
            print(f"{number} x {i} = {number * i}")

    except ValueError:
        print("Error: Number must be a positive integer.")


def tables_to_n():
    try:
        n = int(input("\nEnter N: "))

        if n <= 0:
            print("Error: N must be a positive integer.")
            return

        for number in range(1, n + 1):
            print(f"\nMultiplication Table for {number}:")

            for i in range(1, 13):
                print(f"{number} x {i} = {number * i}")

            print("--------------------")

    except ValueError:
        print("Error: N must be a positive integer.")


# Main Program
single_table()
tables_to_n()