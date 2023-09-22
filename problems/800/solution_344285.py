def total (lista, dicionario):
    soma = 0
    chaves = list(dict.keys(dicionario))
    valores = list(dict.values(dicionario))
    contador=0
    for c in chaves:
        if lista[contador] in chaves:
            soma = soma + valores[contador]
            contador = 0
    return soma