def total(lista,dicionario):
    total = 0
    for produto in lista:
        total += dicionario[produto]
    return round(total,2)