def total (lista_de_compra, dicionario):
    soma = 0 
    for produto in dicionario:
        if produto in dicionario:
            soma += 2
    return round(soma, 2)