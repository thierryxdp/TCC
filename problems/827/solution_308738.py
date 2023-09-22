def qtd_divisores (n):
    ''' Dado um numero n, retorna quantos divisores esse numero tem'''
    if n==0 or n<0:
        return 0
    lista=list(range(1,n+1))
    for x in lista:
        if n%x == 0:
            divisores = len(x)
            return divisores