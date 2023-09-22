def fatorial(num):
    teste = 1
    contador = 1
    t1 = 0
    while contador<=num:
        teste = teste*num
        contador += 1
        t1 = num-1
    return teste