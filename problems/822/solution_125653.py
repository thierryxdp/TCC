def repetidos(lista,n):
    ''' a funcao recebe uma lista e retorna o numeros de vezes que um numero da lista é igual ao numero anterior'''
    '''lista -> int'''
    
    rep = 0
    i = 0
    
    for i in range(len(lista)-1):
        if lista[i] == (lista[i+1]):
            rep = rep + 1
        i = i + 1
    return rep