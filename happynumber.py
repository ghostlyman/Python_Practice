def add(num):
    ret = 0
    for i in str(num):
        ret += (int(i)) ** 2
    return ret

def happy_number(num):
    results = {num}
    ret = num
    while ret >= 10:
        ret = add(ret)
        if ret in results:
            return False
        results.add(ret)
    return ret == 1


for i in range(1, 10000):
    if happy_number(i):
        print('{0} is happy number'.format(i))
