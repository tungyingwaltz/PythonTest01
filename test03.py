Multiples = []

i = 1
while (i<1000):
    if i%3 == 0  or i%5 ==0:
        Multiples.append(i)
    i = i +1

sum = sum(Multiples)
print(sum)