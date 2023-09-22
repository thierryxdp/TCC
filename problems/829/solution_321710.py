def soma_h(n):
    '''Retorna o resultado da formula H=1+1/2+1/3+...+1/N;
       Entrada: int;
       Saida: float;'''
    soma=0
    for x in range(1,n+1):
        soma+=1/x
    return round(soma,2)