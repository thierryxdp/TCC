def total(ls, dic):
    price = 0
    for e in ls:
        price = price + dic[e]
    return price