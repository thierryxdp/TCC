def repetidos(lista):
    qnt_elementos = 0
    i = 1
    j = i - 1
    while j<len(lista) + 1:
        if lista[i] == lista[j]:
             qnts_elementos = qnts_elementos + 1
           i = i + 1
           j = j + 1
    return qnts_elementos