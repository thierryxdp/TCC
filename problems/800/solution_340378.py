def total(lista,dic):
    i = 0
    soma = 0
    for lista[i] in dic:
        soma = soma + dic[lista[i]]
        i = i + 1
    return soma