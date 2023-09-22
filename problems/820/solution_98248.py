def posLetra(frase, letra, n):
    i = 0
    frase_l = list(frase)
    count = 0
    
    while i < len(frase_l):
        if frase_l[i] == letra:
            count += 1
        if count == n:
            return i
        i += 1
    
    if count == 0:
        return -1