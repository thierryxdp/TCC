def qtd_divisores (n):
    ''' Dado um numero n, retorna quantos divisores esse numero tem'''
    if n==0 or n<0:
        return 0
    i=0
    for i in list(range(1,n+1)):
        if n%i == 0:
            return list.count(n,i)