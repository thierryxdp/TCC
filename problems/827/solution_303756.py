def qtd_divisores(n):
    for i in range(1, int(num/2+1)):
        if num % i == 0: 
            return i
    return num