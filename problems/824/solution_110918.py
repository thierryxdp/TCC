def uppCons(f):
    contador = 0
    f1 = ''
    while contador < len(f):
        if f[contador]  != 'AEIOUaeiou':
            f1 = f1 + f[contador].upper()
        contador = contador + 1
    return f1