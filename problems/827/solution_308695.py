def qtd_divisores (n):
    ''' Dado um numero n, retorna quantos divisores esse numero tem'''
    if n==0 or n<0:
        return 0
    for num in range(1,n+1):
        if n%num == 0:
            divisores = len(num)
            return divisores