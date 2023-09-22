def repetidos(lista=[]):
    '''Funcao que recebe uma lista de numeros, e retorna o numero de vezes que um elemento da lista é igual ao anterior.
    List -> Int'''
    num = 0
    tam = len(lista)
    a = 0
    
    while a < tam:
        if a > 0 and lista[a] == lista[a-1]:
            num = num + 1
            a = a+1
    return num