def total(lista, dicionario):
    dicionario = { }
    soma = 0
    for x in lista:
        if x in dicionario:
            dicionario = {x}
    return sum(dicionario)