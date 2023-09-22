def total(lista,precos):
    numero = 0
    for i in lista:
        if lista[i] == precos.keys():
            numero += precos[i]
    return round(numero, 2)