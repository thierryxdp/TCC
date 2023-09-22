def soma_h(N):
    """ Dado H = 1+1/2+1/3+1/4+...+1/N, essa função receberá
    o valor inteiro N como parâmetro de entrada e retornará
    o valor de H.
    
    int -> int
    """
    
    i = 1
    j = 1
    for n in range(1,N+1):
        if n >= 0:
            i = 1/(i+1)
        j = j + i
    return j