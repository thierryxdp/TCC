def posLetra(string,letra,n):
    i = 0
    acumulador= 0
    while i<len(string) and acumulador<n:
        if string[i] == letra:
            acumulador=acumulador +1
        i = i + 1
    if acumulador<n:
        return (acumulador)+(string)
    else:
        return -1