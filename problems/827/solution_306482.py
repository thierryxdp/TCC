def tenta_dividir(x,y):
    '''retorna 1 se y eh divisor de x; int, int -> bool'''
    return 1 if x%y==0 else 0
def qnt_divisores(n):
    '''retorna o numero de divisores de n; int -> int'''
    divisores=list(map(tenta_dividir,n*[n],list(range(1,n+1))))
    return sum(divisores)