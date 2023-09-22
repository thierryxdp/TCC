def soma_h(n):
    '''
       Dado n que define o tamanho de H a função retorna a 
       soma dos elementos de H.
       int -> float
    '''
    soma=0
    for i in range(1, n+1):
        inverso = (1/i)
        soma += inverso
    return round(soma, 2)