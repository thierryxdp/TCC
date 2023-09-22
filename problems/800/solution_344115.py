def total(lista,produtos):
    numero = 0
    for i in lista:
        if lista[i] == produtos.keys(i):
            numero += precos[i]
    return round(numero, 2)