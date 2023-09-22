def posLetra(palavra, l, n):
    i = 0
    a = 0
    if l not in palavra:
        return -1
    while i<len(palavra):
        if palavra[i]== l :
            x = i
            a = a + 1
            if a<n:
                return -1
        i = i + 1
    return x