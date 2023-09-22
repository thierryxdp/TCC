def total(lista,dic):
    soma = 0
    for coisa in lista:
        if coisa in dic:
            soma = soma + dic[coisa]
    return soma