def fatorial(n):
    '''
    int ----> int
    função recebe um numero inteiro, e retorna o fatorial
    deste numero inteiro
    '''
    i = 1
    fatorial = 1
    
    while i <=n:
        fatorial = fatorial*i
        i+=1
    
    return fatorial