def total(lista_de_compras,produtos):
    total=0
    for i in range(0,len(lista_de_compras)+1):
        if lista_de_compras[i] in produtos[preco]:
            total=total+produtos[preco]
    return total