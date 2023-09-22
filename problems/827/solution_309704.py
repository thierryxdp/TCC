def qtd_divisores(n):
    '''
    Função que recebe um numero e conta quantos divisores esse
    numero tem
    int--->int
    '''
    d=n-1
    resposta=0
    while d!=0:
        if n%d==0:
            resposta+=1
        d=d-1
    return reposta