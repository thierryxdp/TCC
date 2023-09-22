def qtd_divisores(n):
    '''Escreva um numero inteiro qualquer. A funcao calcula quantos
    divisores esse numero tem.
    int -> int'''
    divisores=0
    for x in range(1,n+1):
        if n%x==0:
            divisores=divisores+1
    return divisores