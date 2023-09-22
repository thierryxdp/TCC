def filtra_pares(a,b,c,d):
    tupla = []

    if a % 2 == 0:
        tupla = tupla + [a]
        if b % 2 == 0:
            tupla = tupla + [b]
            if c % 2 == 0:
                tupla = tupla + [c]
                if d % 2 == 0:
                    tupla = tupla + [d]
                    return tuple(tupla)