def uppCons(f):
    contador = 0
    f1 = ''
    while contador < len(f):
        if f[contador] != 'a'or'e'or'i'or'o'or'u'or'A'or'E'or'I'or'O'or'U':
            f1 = f1 + f[contador].upper()
        else:
            f1 = f1 + f[contador]
        contador = contador + 1
    return f1