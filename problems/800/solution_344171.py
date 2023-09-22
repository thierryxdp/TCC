def total(lista, dic):
    valor=0
    for produto in range(len(lista)):
        x = lista[produto]
        if x in dict.keys(dic):
            valor+=dict.get(dic,x)
    return round(valor,2)