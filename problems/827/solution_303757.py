def qtd_divisores(n):
    for i in range(1, int(n/2+1)):
        if n % i == 0: 
            return i
    return n