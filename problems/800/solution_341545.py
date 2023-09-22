def total(compras,dic):
    for key, val in dic.items():
        dic[key] = sum(val)
        return val