def qtd_divisores(n):
    '''Função que conta quantos divisores um número
    tem.
    n=int->int'''
    soma=0
    divisores=range(1,n+1)
    if n<0:
        return 0
    for x in divisores:
        if n%x==0:
            soma=soma+1
    return soma