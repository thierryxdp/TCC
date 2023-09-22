def total (lista_compra, dicionario):
    soma = 0 
    for produto in dicionario:
        if lista_compra in dicionario:
            soma += 1
    return soma