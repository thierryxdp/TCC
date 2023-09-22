def total(lista,precos):
    i=0
    zero=0
    while i<len(lista):
        if lista[i] in precos:
            zero=zero+precos[lista[i]]
            i=i+1
        else:
            i=i+1
    return round(zero,2)