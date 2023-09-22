def total (lista, dicionario):
    soma = 0
    chaves = list(dict.keys(dicionario))
    valores = list(dict.values(dicionario))
    contador=0
    for c in lista:
        if lista[contador] in chaves:
            soma = soma + valores[contador]
            contador = contador + 1
    return soma