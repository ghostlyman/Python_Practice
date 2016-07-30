def find(origin, items=[3, 4]):
    ret = dict()
    for item in items:
        ret[item] = tuple([idx for idx, e in enumerate(origin) if e == item])
        # for idx, e in enumerate(origin):
        #     if e == item:
        #         ret[item].append(idx)
        ret[item] = tuple(ret[item])
    return ret

print(find([3, 4, 5, 2, 7, 4]))