def soma_h(N):
    """ Dado H = 1+1/2+1/3+1/4+...+1/N, essa função receberá
    o valor inteiro N como parâmetro de entrada e retornará
    o valor de H.
    
    int -> int
    """
    
    i = 1
    termos = range(1,N+1)
    while i < len(termos):
        i = i + float(termos[i]/(i+1))
    return  round(i,2)