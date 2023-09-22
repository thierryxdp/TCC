def total(lista,dic):
    valor = 0
    for item in lista:
        if item in dic:
            valor = valor + dict.get(dic,item)
    return valor