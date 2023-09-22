def total(lista,dicionario):
    valor=0
    for i in range(len(lista)):
        if lista[i] in dicionario:
            valor +=dicionario[lista[i]]
    return round (valor,2)