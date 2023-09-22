def divisores(n):
    '''Funcao que dado um numero n retorna a quantidades de seus divisores '''
    divisor=[]
    divisores=0
    for x in range(1, 9999999):
        if n%x == 0:
            list.append(divisor,n/x)
            divisores= len(divisor)
        if n<0:
            return 0
    return divisores