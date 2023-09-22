def qtd_divisores(num):
    cont = 0
    for i in range(1, num):
        if num%i == 0:
            cont = cont + 1
    return cont