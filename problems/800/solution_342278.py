def total(compras,dic):
    soma = 0
    i=0
    for i in range(len(compras)):
        if compras[i] in dict.keys(dic):
            a = dict.get(dic,compras[i])
    soma = soma + a
    return soma