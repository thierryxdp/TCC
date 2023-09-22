def total(lista, dic):
    soma = 0
    for i in range(len(lista)):
        if lista[i] in dic:
            soma = soma + dic[lista[i]]
    return round(soma, 2)