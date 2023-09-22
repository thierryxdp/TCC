def total(lista, dic):
    soma = o
    for i in len(lista):
        if lista[i] in dic:
            soma = soma + dic[lista[i]]
    return soma