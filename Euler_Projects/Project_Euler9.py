# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2.
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math

while True:
    for i in range(1, 1000):
        for k in range(1, 1000):
            c = i ** 2 + k ** 2
            result = i + k + math.sqrt(c)
            if result == 1000:
                print(i * k * math.sqrt(c))
                break
    break
