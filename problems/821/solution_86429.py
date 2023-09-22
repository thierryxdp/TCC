def fatorial():
    " Fatorial de um numero dado."
    print("Cálculo do fatorial de um número\n")
    n = int(input("Digite um número inteiro não-negativo: "))
    n_fat=1
    for i in range(2,n+1):
        n_fat = n_fat*1
        print("%d! = %d" %(n, n_fat))