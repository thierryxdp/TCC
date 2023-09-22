def posLetra(palavra, l, n):
    i = 0
    if l not in palavra:
        return -1
    while i<len(palavra):
        if palavra[i]== l :
            x = i
            a = a + x
        i = i + 1
    return a