def total(lista, dicionario):
    j=0
    for i in lista:
        if i in dicionario:
            j=round(dicionario.get(i),2)+j
    return j