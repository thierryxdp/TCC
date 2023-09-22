def total (lista, dicionario):
    soma = 0
    for c in lista:
        if c in dicionario:
            soma = soma + dicionario[c]
    return round(soma, 2)