# fizzbuzz.py
def fizzbuzz(start, end):
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    while True:
        try:
            start = int(input("Enter the starting number: "))
            end = int(input("Enter the ending number: "))
            if start > end:
                raise ValueError("Starting number must be less than or equal to ending number.")
            fizzbuzz(start, end)
            break  # Exit the loop after successful input
        except ValueError as e:
            print(f"Error: {e}. Please enter valid integers.")
