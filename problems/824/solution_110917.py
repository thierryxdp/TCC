def uppCons(f):
    contador = 0
    while contador < len(f):
        if f[contador]  != 'AEIOUaeiou':
            f[contador].upper()
        contador = contador + 1
    return f