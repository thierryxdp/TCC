def filtraMultiplos(lista,n):
    a = 0
    resultado = []
    while a < len(lista):
        if lista[a]%n == 0:
            resultado = resultado + lista[a]
        a += 1
    return resultado