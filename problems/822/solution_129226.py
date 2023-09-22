def repetidos(lista):
    i = 1
    qnt = 0
    while i < len (lista):
        if lista[i-1] == lista[i]:
            qnt +=1
        i +=1 
    return qnt