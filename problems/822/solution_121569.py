def repetidos(lista):
    '''recebe uma lista de números e retorna o número de vezes que um elemento da lista é igual ao anterior;lista->int'''
    i=1
    contador=0
    while lista[i]<=len(lista):
        if lista[i]==lista[i-1]:
            contador+=1
            i+=1
        elif lista[i]!=lista[i-1]:
            i+=1
    return contador