def posLetra(s,letra,n):
    """
    Retorna a posicao da letra desejada
    """
    i=0
    j=0
    while i<len(s):
        while j<n:
            if letra==s[i]:
                if j==n:
                    return i
            j=j+1
        i=i+1