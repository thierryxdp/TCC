def posLetra(string,l,n):
    m=0
    for letra in string:
        if string[letra]==l:
            m=m+1
        if m==n:
            return letra
    return -1