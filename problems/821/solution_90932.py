def fatorial(num):
    contador = 1
    fat = 1

    while contador <= num:
        fat *= contador
        contador += 1
        print(fat)

    return fat