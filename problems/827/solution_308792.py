def qtd_divisores (n):
    ''' Dado um numero n, retorna quantos divisores esse numero tem'''
    if n==0 or n<0:
        return 0
    i=0
    num= list(range(1,n+1))
    lista=len(num)
    for i in lista:
        if lista%n == 0:
            divisores = len(lista)
            return divisores