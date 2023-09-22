def total(lista,dic):
    for coisa in lista:
        if coisa in dic:
            soma = soma + dic[coisa]
    return soma