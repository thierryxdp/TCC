def repetidos(lista):
    '''
    Recebe uma lista de numeros int 
    Retorna um int como o número de vezes que  um elemento foi repetido na lista
    '''
    N_elementos=0
    for i in range(len(lista)):
        if lista[i]==lista[i-1]:
            N_elementos+=1
    return N_elementos