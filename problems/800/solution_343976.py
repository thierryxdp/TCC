def total(lista,dicionario):
    valor = 0
    for x in lista:
        if x in dicionario:
            valor = valor + dicionario[x]
    return round(valor,2)