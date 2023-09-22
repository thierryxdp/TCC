def total(lista, produtos):
    soma = 0
    for i in lista:
        if i in produtos:
            soma = soma + produtos[i]
    return round(soma,2)