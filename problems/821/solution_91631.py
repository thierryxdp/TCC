def fatorial(num):
    teste = 1
    contador = 1
    while contador<=num:
        teste = teste*num
        contador += 1
        num = num-1
    return teste