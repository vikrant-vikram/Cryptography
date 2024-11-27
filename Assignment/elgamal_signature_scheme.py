import random
from sympy import isprime, mod_inverse




def handler():
    print("======== Welcome to the ElGamal Signature System ========")

    # Step 1: Input a prime number
    while True:
        try:
            prime = int(input("Enter a prime number (p): "))
            if isprime(prime):
                break
            else:
                print("The entered number is not prime. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Generate keys
    prime, generator, public_key, private_key = generate_keys(prime)
    print("\nGenerated Keys:")
    print(f"  Public Key: (p={prime}, g={generator}, y={public_key})")
    print(f"  Private Key: x={private_key}")

    # Step 2: Enter a message
    while True:
        try:
            message = int(input(f"\nEnter a message to sign (0 ≤ m < {prime-1}): "))
            if 0 <= message < prime - 1:
                break
            else:
                print(f"Message must be between 0 and {prime-2}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Create signature
    r, s = sign_message(prime, generator, private_key, message)
    print(f"\nDigital Signature:")
    print(f"  r = {r}")
    print(f"  s = {s}")

    # Verify signature
    print("\nVerifying the signature...")
    is_valid = verify_signature(prime, generator, public_key, message, r, s)
    if is_valid:
        print(f"\033[32mSignature is valid!\033[0m")  # Green text for valid
    else:
        print(f"\033[31mSignature is invalid!\033[0m")  # Red text for invalid

    # Experiment with modifications
    while True:
        modify = input("\nDo you want to test with modified values? (yes/no): ").strip().lower()
        if modify == "yes":
            print("Options: [1] Change message, [2] Change r, [3] Change s")
            option = input("Select an option: ").strip()
            if option == "1":
                new_message = int(input(f"Enter a new message (0 ≤ m < {prime-1}): "))
                is_valid = verify_signature(prime, generator, public_key, new_message, r, s)
                result = "Valid" if is_valid else "Invalid"
                color = "\033[32m" if is_valid else "\033[31m"
                print(f"{color}Verification with modified message: {result}\033[0m")
            elif option == "2":
                new_r = int(input(f"Enter a new value for r (1 ≤ r < {prime}): "))
                is_valid = verify_signature(prime, generator, public_key, message, new_r, s)
                result = "Valid" if is_valid else "Invalid"
                color = "\033[32m" if is_valid else "\033[31m"
                print(f"{color}Verification with modified r: {result}\033[0m")
            elif option == "3":
                new_s = int(input(f"Enter a new value for s (0 ≤ s < {prime-1}): "))
                is_valid = verify_signature(prime, generator, public_key, message, r, new_s)
                result = "Valid" if is_valid else "Invalid"
                color = "\033[32m" if is_valid else "\033[31m"
                print(f"{color}Verification with modified s: {result}\033[0m")
            else:
                print("Invalid choice. Please select a valid option.")
        elif modify == "no":
            print("Thank you for using the ElGamal Digital Signature System. Goodbye!")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

# Function to locate a generator (primitive root) modulo p
def get_generator(prime):
    if not isprime(prime):
        raise ValueError("The input must be a prime number.")

    totient = prime - 1
    prime_factors = get_prime_factors(totient)

    for candidate in range(2, prime):
        if all(pow(candidate, totient // factor, prime) != 1 for factor in prime_factors):
            return candidate

    raise ValueError("Failed to find a generator.")

# Function to determine the prime factors of a given number
def get_prime_factors(number):
    factors = set()
    divisor = 2
    while divisor * divisor <= number:
        while number % divisor == 0:
            factors.add(divisor)
            number //= divisor
        divisor += 1
    if number > 1:
        factors.add(number)
    return factors

# Generate keys for the ElGamal scheme
def generate_keys(prime):
    generator = get_generator(prime)
    private_key = random.randint(1, prime - 2)  # Private key: 1 ≤ x ≤ p−2
    public_key = pow(generator, private_key, prime)  # y = g^x mod p
    return (prime, generator, public_key, private_key)

# Create a digital signature for a given message
def sign_message(prime, generator, private_key, message):
    while True:
        random_k = random.randint(1, prime - 2)
        if compute_gcd(random_k, prime - 1) == 1:
            break

    r = pow(generator, random_k, prime)
    k_inverse = mod_inverse(random_k, prime - 1)
    s = (k_inverse * (message - private_key * r)) % (prime - 1)
    return (r, s)

# Verify a digital signature
def verify_signature(prime, generator, public_key, message, r, s):
    lhs = (pow(public_key, r, prime) * pow(r, s, prime)) % prime
    rhs = pow(generator, message, prime)
    return lhs == rhs

# Compute the greatest common divisor
def compute_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Main program for user interaction
if __name__ == "__main__":
    handler()
