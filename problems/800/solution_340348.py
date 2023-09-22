def total(lista,produtos):
    soma=0
    i=0
    for x in produtos:
        if lista[i] == x:
            soma=soma+produtos[x]
        i=i+1
    return soma