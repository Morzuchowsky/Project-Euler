# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def prime_sum(limit):
    sieve = [True] * limit
    sieve[0], sieve[1] = False, False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False
    return sum(i for i, is_prime in enumerate(sieve) if is_prime)


print(prime_sum(2000000))
