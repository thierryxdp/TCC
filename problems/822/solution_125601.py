def repetidos(listanumeros):
    
    '''Função que  partir de uma lista de números retorna a quantidade de vezes que um item dessa lista é igula ao item anterior. list -> int'''
    
    i = 0
    k = 0
    
    while i < (len(listanumeros) - 1):
        if listanumeros[i] == listanumeros[(i+1)]:
            k = k + 1
        i = i + 1
    
    return k