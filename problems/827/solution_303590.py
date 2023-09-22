import math
def qtd_divisores(n):
    '''Função que conta quantos divisores um número possui
    int->int'''
 d = [1]
    if n<0:
            return 0
    for i in range(2,int(math.sqrt(n))+1):

        if n%i == 0:
            d.extend([i,n/i])
    d.extend([n])
    a=list(set(d))
    return len(a)