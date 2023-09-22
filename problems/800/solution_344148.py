def total (lista, dicionario):
    soma = 0 
    dicionario = list(dicionario)
    for produto in dicionario:
        if produto in dicionario:
            soma = soma + produto
        return soma