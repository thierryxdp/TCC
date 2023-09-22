def total(lista, dicionario):
    list = ( )
    soma = 0
    for x in lista:
        if x in dicionario:
            soma = sum(x)
    return round(soma,2)