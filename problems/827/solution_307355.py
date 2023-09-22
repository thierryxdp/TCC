def qtd_divisores(n):
    '''Retorna a quantidade de divisores que n possui
int -> int'''
    divisores=0
    for x in list(range(1,n+1)):
        if n%x==0:
            divisores=divisores+1
    return divisores