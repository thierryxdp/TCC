def soma_h(N):
    """ Dado H = 1+1/2+1/3+1/4+...+1/N, essa função receberá
    o valor inteiro N como parâmetro de entrada e retornará
    o valor de H.
    
    int -> int
    """
    
    n = []
    j = 1
    for i in range(1,N+1):
        if i >= 0:
            i = 1/(i+1)
            n = n + [i,]
        m = sum[n]    
        j = j + m
    return j