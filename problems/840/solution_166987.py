def bolos(A,B,C):
    '''
    funcao que calculaa quantidade de bolos que joao pode fazer
    param: A,B,C: float
    retorna: qtd bolos: int
    '''
    #farinha = 2a
    #ovos = 3b
    #leite = 5c
    #(2a+3b+5c)=1 bolo

    return min(A//2,B//3,C//5)