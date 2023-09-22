def total(lista,dicionario):
    i=0
    valor=0
    while i<len(lista):
        a=float(dicionario.get(lista[i]))
        valor=valor+a
        i=i+1
    return round(valor,2)