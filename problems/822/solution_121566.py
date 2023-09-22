def repetidos(lista):
    '''recebe uma lista de números e retorna o número de vezes que um elemento da lista é igual ao anterior;lista->int'''
    i=0
    contador=0
    while lista[i]<len(lista):
        if lista[i]==lista[1+i]:
            contador+=1
            i+=1
        elif lista[i]!=lista[1+i]:
            i+=1
    return contador