def total(lista_de_compras,produtos):
    total=0
    i=0
    for i in range(0,len(lista_de_compras)+1):
        if lista_de_compras[i] in produtos:
            total=total+produtos[lista_de_compras[i]]
            i=i+1
    return total