# inflect module required

"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one
hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British
usage."""


import inflect


p = inflect.engine()

sum_of_digits = 0
for i in range(1, 1001):
    temp = p.number_to_words(i)
    clean_temp = temp.replace("-", "").replace(" ","").replace("and ", "")
    sum_of_digits += len(clean_temp)

print(sum_of_digits)
