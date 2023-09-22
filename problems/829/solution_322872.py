def soma_h(n):
    '''
       função que recebe um numero inteiro (n) e retorna o 
       valor da seguinte soma (1 + 1/2 + 1/3 + 1/4 + ... 1/n)
       int -> float
    '''
    soma=0
    termos=list(range(n))
    termos.append(n)
    termos.remove(0)
    for i in termos:
        soma+=(1/i)
    return round(soma,2)