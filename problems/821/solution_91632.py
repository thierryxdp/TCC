def fatorial(num):
    teste = 1
    contador = 1
    while contador<=num:
        teste = teste*num
        num = num-1
        contador += 1
    return teste