def posLetra(frase,letra,n):
    a = 0
    b = 0
    f = []
    while a < len(frase):
        if b <= n-1:
            if str.upper(letra) == str.upper(frase[a]):
                f += [frase[a]]
                b += 1
            a += 1
        else:
            a += 1
    return f