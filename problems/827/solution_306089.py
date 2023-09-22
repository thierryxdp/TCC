def qtd_divisores(n):
    totalDeDivisores = 0
    for numero in range(n):
        if(numero % n) == 0:
            totalDeDivisores += 1
    return totalDeDivisores