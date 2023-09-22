def total (lista_de_compra, dicionario):
    soma = 0 
    for produto in lista_de_compra:
        if produto in dicionario:
            soma = soma + dicionario
    return soma