def is_prime(number):
    # ctrl+i to ask the VS code in AI chat
    """Check if a number is a prime number."""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example usage
if __name__ == "__main__":
    num = int(input("Enter a number to check if it's prime: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")