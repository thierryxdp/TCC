def total(lista,produtos):
    numero = 0
    for i in lista:
        if lista[i] == produtos.values():
            numero += produtos[i]
    return round(numero, 2)