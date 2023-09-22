def fatorial(numero):
    """retorna o fatorial do número
    int -> int"""
    contador = 1
    fat = 1

    while contador <= numero:
        fat *= contador
        contador += 1
        print(fat)

    return fat