def qtd_divisores(n):
    '''retorna quantos divisores o numero n possui; int -> int'''
    soma=1
    if n<0:
        return 0
    for numero in range(1,n):
        if n%numero==0:
            soma=soma+1
    return soma