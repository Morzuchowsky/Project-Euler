# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def is_prime(num_1):
    for i in range(2, num_1):
        if num_1 % i == 0:
            return False
    return True


def prime_range():
    num_2 = 2
    final_sum = 0
    while num_2 < 2000000:
        if is_prime(num_2):
            final_sum += num_2
        num_2 += 1
    return final_sum


print(prime_range())
