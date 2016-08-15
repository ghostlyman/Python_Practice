#Print Prime Number from 10 to 20

for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num/i
            print('%d = %d * %d' % (num, i, j))
    else:
        print(num, 'is Prime Number')