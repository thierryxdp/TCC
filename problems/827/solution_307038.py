def qtd_divisores(n):
    '''
       Funcao que retorna quantos divisores um numero tem.
       int -> int
    '''
    qtd = 0
    for elem in range(1,n+1):
        if n % elem == 0:
            qtd = qtd + 1
    return qtd