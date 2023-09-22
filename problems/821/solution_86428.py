def fatorial():
    " Fatorial de um numero dado."
    print("Cálculo do fatorial de um número\n")
    n = int(input("Digite um número inteiro não-negativo: "))
    i = 1  
    n_fat=1
    while i <= n:
        n_fat = n_fat * i 
        i = i + 1
    print("%d! = %d" %(n, n_fat))