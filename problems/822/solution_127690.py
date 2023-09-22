def repetidos(lis):
    '''
    Funçao que recebe uma lista e retorna o numero de vezes
    que o numero da lista é igual ao numero anterior
    lis -> int
    '''
    i=0
    x=0
    while i< len(lis):
        if lis[i] == lis[i-1]:
            x= x+1
    	i=i+1
    return x