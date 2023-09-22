def total(lista,dicionario):
    valor = 0
    for produtos in lista:
        valor = valor + dicionario[produtos]
    return valor