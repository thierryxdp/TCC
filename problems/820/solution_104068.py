def posLetra(frase, letra, n):
    i = 0
    occ = 0
    found = False
    pos = -1
    
    while i < len(frase) and found is False:
        if frase[i] == letra:
            occ += 1
            if occ == n:
                found = True
                pos = i
        i += 1
    
    return pos