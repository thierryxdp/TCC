def total(lista,produtos):
    soma=0
    i=0
    for x in produtos:
        if i<len(lista) and lista[i] == str(x):
            soma=soma+produtos[x]
        i=i+1
    return soma