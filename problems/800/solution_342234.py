def total(lista, dicionario):
    soma = 0
    for i in range(len(lista)):
        if lista[i] in dicionario:
            soma += dicionario[lista[i]]
    return round(soma,2)