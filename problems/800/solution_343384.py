def total(lista,dicio):
    ''''''
    total = 0
    for i in range(len(dicio)):
        if lista[i] in dicio:
            total = total + dict.get(dicio,lista[i])
    return round(total,2)