def total(lista,dicionario):
    valor=[]
    for i in range(len(lista)):
        if lista[i] in dicionario:
            valor.append(dicionario[lista[i]])
    return round(sum(valor),2)