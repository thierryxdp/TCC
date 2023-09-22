def posLetra(frase,l,n):

    i = 0
    if l in frase:
        while i < len(frase):
            if l == frase[i]:
                n = n-1
                i = i+1
            if l != frase[i]:
                i = i+1
            if n == 0:
                return i - 2
            
    return -1