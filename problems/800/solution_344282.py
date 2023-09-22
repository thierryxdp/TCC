def total (lista, dicionario):
    soma = 0
    chaves = list(dict.keys(dicionario))
    valores = list(dict.values(dicionario))
    for c in chaves:
        if lista[0] in chaves:
            soma = soma + valores[0]
    return soma