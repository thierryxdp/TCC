def total(lista = [], dic = {}):
    dic = {}
    cont = 0.0
    for i in lista:
        cont+=dic[i]
    return round(cont, 2)