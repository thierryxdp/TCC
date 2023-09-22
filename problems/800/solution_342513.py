def total(lista, dicionario):
    list = []
    for elemento in lista:
        if elemento in dicionario:
            list.append(elemento)
    soma = sum(list)
    return round(soma, 2)