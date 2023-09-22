def fatorial(num):
    contador = 1
    teste = 1
    while contador<len(num):
        teste = teste*num[contador]
        contador += 1
    return teste