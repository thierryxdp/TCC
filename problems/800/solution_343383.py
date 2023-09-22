def total(lista,dicio):
    ''''''
    total = 0
    for i in dicio:
        if lista[i] in dicio:
            total = total + dict.values(dicio[i])