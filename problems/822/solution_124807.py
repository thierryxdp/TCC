def repetidos(lista):
    '''   '''
    quantidade = 0
    for i in range(len(lista)-1):
        if lista[i] == lista[i+1]:
            quantidade +=1
    return quantidade