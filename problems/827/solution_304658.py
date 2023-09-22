def qtd_divisores (n):
    qtdN = 0
    for i in range(1,n+1):
        if n % i :
            qtdN = qtdN + 1
 		return qtdN