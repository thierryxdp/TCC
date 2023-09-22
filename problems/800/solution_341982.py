def total(listaCompras,produtos):
    soma=0
    for i in range(len(listaCompras)):
        if listaCompras[i] in produtos:
            soma=soma+produtos[listaCompras[i]]
    return round(soma,2)