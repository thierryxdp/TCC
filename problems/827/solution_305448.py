def qtd_divisores(n):
    divisores = list()
    divisores.append(n)
    for i in range(1, int(n/2+1)):
        if n % i ==0:
            divisores.append(i) 
    return len(divisores)