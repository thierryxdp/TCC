def uppCons(frase):
    n = len(frase)

    while n >=0:
        n=n-1
        if frase[n] != a and frase[n] != e and frase[n] != i and frase[n] != o and frase[n] != u:
            caracter = str.upper(frase[n])
            frase1=frase.replace(frase[n],caracter,n)

    return frase