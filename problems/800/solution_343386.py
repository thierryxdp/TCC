def total(lista,dicio):
    ''''''
    total = 0
    s=str(lista)
    for i in range(len(dicio)):
        if str.find(lista,i) in dicio:
            total = total + dict.get(dicio,lista[i])
    return round(total,2)