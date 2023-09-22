def total(lista,produtos):
    soma=0
    for x in produtos:
        if lista == x:
            soma=soma+produtos[x]
    return soma