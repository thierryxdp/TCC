qtd_divisores(n):
    '''função que retorna quantos divisores o número n tem.
    entrada:int
    saída:int'''
    d=0
    for i in range(1,n+1):
        if n%i==0:
            d=d+1
    return d