def total (lista, dicionario):
    soma = 0
    for c in lista:
        if c in dicionario:
            soma = soma + dict.values(dicionario)
    return soma