"""
"2 to the power of 15 is 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26."

"What is the sum of the digits of the number 2 to the power of 1000?"
"""

final_sum = 0
for i in str(pow(2, 1000)):
    final_sum += int(i)
print(final_sum)
