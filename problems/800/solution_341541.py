def total(compras,dic):
    total = sum(filter(lambda elem:elem,(map(lambda dic:float(dic),dic.values()))))
    return