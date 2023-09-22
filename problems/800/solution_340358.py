def total(lista,produtos):
    soma=0
    for x in produtos:
        if x in lista:
            soma=soma+produtos[x]
    return round(soma,2)