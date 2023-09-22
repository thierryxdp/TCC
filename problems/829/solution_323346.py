def soma_h(N):
    """ Dado H = 1+1/2+1/3+1/4+...+1/N, essa função receberá
    o valor inteiro N como parâmetro de entrada e retornará
    o valor de H.
    
    int -> int
    """
    
    n = 0
    j = 0
    for i in range(0,N):
        if i == n:
            n = n + 1
            j = j + 1/(n+1)
        x = 1 + j
    return round(x,2)