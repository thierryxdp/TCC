def fatorial():
    '''Programa que lê um número inteiro n >= 0 e imprime n!, int>int'''

    print("Cálculo do fatorial de um número\n")

    n = int(input("Digite um número inteiro não-negativo:"))
	n_fat = 1
    for i in range(2,n+1):
        n_fat = n_fat * i 

    print("%d! = %d" %(n, n_fat))