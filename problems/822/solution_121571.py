def repetidos(lista):
    '''recebe uma lista de número e retorna o número de vezes que um elemento da lista é igual ao anterior;lista->int'''
    i=1
    contador=0
    while len(lista)>i:
        if lista[i]==lista[i-1]:
            i+=1
            contador+=1
        else:
            i+=1
    return contador