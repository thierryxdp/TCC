def qtd_divisores(num):
    qtd = 0
    for div in range(num+1):
        if div !=0:
            if num % div == 0:
                qtd = qtd + 1
    return qtd