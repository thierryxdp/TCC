def total(lista,dicionario):
    i=0
    while i<len(lista):
        a=int(dicionario.get(lista[i]))
        valor=valor+a
        i=i+1
    return valor