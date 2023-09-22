def divisores(n):
    '''Funcao que dado um numero'n' retorna a quantidade de seus divisores '''
    divisor=[]
    divisores=0
    for x in range(1,1000000000000000000000):
        if n%x == 0:
            list.append(divisor,n/x)
            divisores= len(divisor)
    return divisores