def total(lista,dicionario):
    valor=[]
    for c in lista:
        valor.append(dicionario[c])
    return round(sum(valor),2)