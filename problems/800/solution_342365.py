def total(lista, dicionario):
    soma=0
    for item in lista:
        soma=soma+dict.get(dicionario, item)
    return round(soma, 2)