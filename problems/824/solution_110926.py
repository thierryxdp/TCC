def uppCons(f):
    contador = 0
    f1 = ''
    while contador < len(f):
        if f[contador] != 'a'and'e'and'i'and'o'and'u'and'A'and'E'and'I'and'O'and'U':
            f1 = f1 + f[contador].upper()
        else:
            f1 = f1 + f[contador]
        contador = contador + 1
    return f1