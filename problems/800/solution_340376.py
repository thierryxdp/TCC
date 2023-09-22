def total(lista,dic):
    i = 0
    soma = 0
    while i <= len(dic):
        if lista[i] in dic:
            soma = soma + dic[lista[i]]
        i = i + 1
    return soma