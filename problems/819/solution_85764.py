def filtramultiplos(lista,n):
    multip = []
    contador = 0
    while contador < len(lista):
        if lista[contador] % n == 0:
            multip.insert(contador, lista[contador])
            contador= contador + 1
    return multip