def total(lista,produtos):
    numero = 0
    for i in lista:
        if lista[i] == produtos.keys():
            numero += produtos[i]
    return round(numero, 2)