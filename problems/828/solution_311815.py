def divisores(n):
    divisor = []
    divisores=0
    for x in range(1,n):
        if n%x==0:
            list.append(divisor,n/x)
            divisores=len(divisor)
        if n<0:
            return 0
    return divisores
def primo(n):
    '''Funcao que dado um numero retorna se ele é primo ou nao.
    int->bool'''
    if divisores(n)>1:
        return False
    else:
        return True