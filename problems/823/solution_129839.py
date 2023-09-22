def faltante(quebra_cabeca):
    '''
        Função que descubre qual número inteiro do intervalo está faltando.
        lista(int) => int
    '''
    n = len(quebra_cabeca) + 1
    faltando = n
    quebra_cabeca.sort()
    
    for i in range(1, n):
        if(quebra_cabeca[i-1] != i):
            faltando = i
            break    
    return faltando