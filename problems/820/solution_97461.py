def posLetra(frase,l,n):

    i = 0
    if l in frase:
        while n > 0:
            if l == frase[i]:
                n = n-1
                i = i+1
            if l != frase[i]:
                i = i+1
            if n == 0:
                return i - 2
    else:
        return -1