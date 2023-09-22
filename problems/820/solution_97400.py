def posLetra(frase,letra,oco):
    i = 0
    pos = 0
    while i<len(frase) and pos<oco:
        if frase[i] in letra:
            pos += str.find(letra)
        i += 1
    return pos[oco-1]