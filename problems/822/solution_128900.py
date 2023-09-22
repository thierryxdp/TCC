def repetidos(lista=[]):
    '''Funcao que recebe uma lista de numeros, e retorna o numero de vezes que um elemento da lista é igual ao anterior.
    List -> Int'''
    num = 0
    for a in range(len(lista)):
        if a>0 and lista[a]==lista[a-1]:
            num = num+1
            
    return num