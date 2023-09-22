def repetidos (lista):
    '''numero de vezes que um elemento da lista e igual ao anterior'''
    i=0
    contador=0
    repete=0
    while contador < len(lista):
        if lista[i]==lista[i -1]:
            repete +=1
        i +=1
        contador +=1
    return repete