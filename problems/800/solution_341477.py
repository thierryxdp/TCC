def total(lista, dic):
    contador = 0
    valor = 0
    
    for produtos in lista:
        if lista[contador] in dic:
            valor += dic[lista[contador]]
            contador += 1
    return round(valor, 2)