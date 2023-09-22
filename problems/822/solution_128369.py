def repetidos(lista):
    qnt = 0
    i = 0
    while i < len(lista):
        if lista[i] == lista[i+1]:
            qnt +=1
    	i +=1
    return qnt
# repetidos([1,2,2,2,3,3,3,4,4,1,0])#