def total(lista,dic):
    total = 0
    cont= 0
    for elementos in lista:
        if lista[cont] in dic:
            total += dic [lista[cont]]
            cont+= 1
    return round (total, 2)