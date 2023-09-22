def qtd_divisores(n):
    contador_divisores = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            contador_divisores += 1
            
            return qtd_divisores