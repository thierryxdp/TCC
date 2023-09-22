def qtd_divisores(numero): 
    divisores = 0
    for num in range(1, numero + 1):
        if numero % num == 0:
            divisores += 1
        else:
            pass
    return divisores