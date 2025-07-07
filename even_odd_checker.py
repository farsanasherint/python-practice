# even_odd_checker.py

def check_even_odd(number):
    """
    Checks if a number is even or odd.
    Returns 'Even' or 'Odd' accordingly.
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
if __name__ == "__main__":
    num = 7
    result = check_even_odd(num)
    print(f"The number {num} is {result}.")
