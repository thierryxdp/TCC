def total(lista_compras, produtos_precos):
    x = len(lista_compras)
    i = 0
    total = []
    
    for i in range(x):
        if i < x:
            list.append(total, produtos_precos[lista_compras[i]])
            i += 1
    j = 0
    soma = 0
    while j < len(total):
        soma = soma + total[j]
        j += 1
    return round(soma, 2)