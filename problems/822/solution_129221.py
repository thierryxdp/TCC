def repetidos(lista):
    i=0
    qnt = 0
    while i< len(lista):
        if lista.count(lista[i])>0:
            qnt = qnt + 1
        i +=1
    return  qnt