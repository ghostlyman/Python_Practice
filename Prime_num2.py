#The second method for Prime Number

i = 2
while (i < 20):
    j = 2
    while(j<= (i/j)):
        if not(i%j):
            break
        j = j + i
    if (j > (i/j)):
        print(i, 'is Prime Number')
    i = i + 1
