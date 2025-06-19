def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_primes_up_to(limit):
    primes = []
    for num in range(2, limit + 1)
        if is_prime(num):
            primes.append(num)
    return primes

if __name__ == "__main__":
    print("Primes up to 10:", get_primes_up_to(10))
