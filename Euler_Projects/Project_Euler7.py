# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13
# What is the 10001'st prime number?
def is_prime(num_1):
    for i in range(2, num_1):
        if num_1 % i == 0:
            return False
    return True


def prime_range():
    num_2 = 1
    list_of_primes = []
    while len(list_of_primes) < 10002:
        if is_prime(num_2):
            list_of_primes.append(num_2)
        num_2 += 1
    return list_of_primes


print(prime_range())

