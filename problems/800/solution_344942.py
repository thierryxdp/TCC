def total(lista, dicionario):
    j=0
    for i in lista:
        if i in dicionario:
            j=dicionario.get(i)+j
    return j