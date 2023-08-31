# The four adjacent digits in the 1000-digit number that have the greatest product are 9 x 9 x 8 x 9 = 5832.
# <the 1000-digit number (long)>
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product?

num = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494959501737958331952853208805511125406987471585238630507156932909632952274430435576689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749303589072962904915604407723907138105158593079608667017242712188399879790879227492190169972088809377665727333001053367881220235421809751254540594752243525849077116705560136048395864467063244157221553975369781797784617406495514929086256932197846862248283972241375657056074850246140797296865241453510047482166370484403199890008895243450658541227588666881164271714799442928230863465674813919123128245861786645835912456652947654568284891288314260769004224219022671055626321111109370544217506941658960408071984038509624554432981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

temp = 1
final = 0
for i in range(0, len(num)):
    substring = num[i:i+13]
    if len(substring) > 12:
        for k in substring:
            temp *= int(k)
        if final < temp:
            final = temp
        temp = 1
print(final)