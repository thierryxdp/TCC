def filtrarMultiplos(lista, n):
    lista = []
    numero = 1
    while numero >= n :
        if numero&n ==0:
            numero = numero + 1
            continue
        lista.append(numero)
        numero = numero + 1
    return lista