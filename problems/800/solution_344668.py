def total(lista, valores):
    i = 0
    valor_total = 0 
    for elementos in lista:
        if lista[i] in valores:
            valor_total = valor_total + valores[lista[i]]
            i = i + 1
    return round(valor_total,2)