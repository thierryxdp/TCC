def primo(n):
    
    contadorDivisoes = 0
    
    #Começa no dois, pois, São considerados números primos 
    #os termos numéricos maiores que 1, divisíveis por 1 e por ele mesmo
    for i in range(2, n):
        if n % i == 0:
            contadorDivisoes += 1
    
    if n == 1:
        print("O numero ", n, " NÃO é primo")
    elif n == 0:
        print("O numero ", n, " NÃO é primo")
    elif contadorDivisoes == 0:
        print("O numero ", n, " é primo")
    else: 
        print("O numero ", n, " NÃO é primo")