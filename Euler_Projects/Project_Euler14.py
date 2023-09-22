"""
The following iterative sequence is defined for the set of positive integers:
n→n/2n→n/2 (nn is even)
n→3n+1n→3n+1 (nn is odd)
Using the rule above and starting with 1313, we generate the following sequence:
13→40→20→10→5→16→8→4→2→1
It can be seen that this sequence (starting at 1313 and finishing at 11) contains 1010 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 11.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""

final = {}

for n in range(1, 1_000_000):
    temp = n
    counter = 1
    while temp != 1:
        if temp % 2 == 0:
            temp = temp / 2
            counter += 1
        else:
            temp = temp * 3 + 1
            counter += 1
    final[n] = counter

max_key = max(final.keys(), key=lambda k: final[k])
print("Liczba", max_key, "ma najdłuższy ciąg o długości", final[max_key])