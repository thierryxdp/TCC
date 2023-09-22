def fatorial(n):
    '''
    Programa que lê um número inteiro n >= 0 e imprime n!
    '''
n = int(input("Digite um número inteiro não-negativo: "))
i= 1
n_fat = 1
    while i <= n:
        n_fat = n_fat * i 
        i = i + 1
    return("%d! = %d" %(n, n_fat))