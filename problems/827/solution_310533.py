def qtd_divisores(num):
    cont = 0
    for divisor in range (1, num) :
        if num % divisor == 0:
            cont+= 1
    if num <= 0:
        return cont
    else:
        return cont + 1