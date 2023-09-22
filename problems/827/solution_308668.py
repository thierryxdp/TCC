def qtd_divisores (n):
    ''' Dado um numero n, retorna quantos divisores esse numero tem'''
    if n==0:
        return 0
    for i in range(1,n):
        if n%i == 0:
            return len(i)