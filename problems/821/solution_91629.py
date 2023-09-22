def fatorial(num):
    teste = 1
    contador = 1
    t1 = num
    while contador<=t1:
        teste = teste*num
        contador += 1
        t1 = t1 - 1
    return teste