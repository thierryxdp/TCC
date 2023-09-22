def posLetra(frase,letra,oco):
    i=0
    pos=0
    while i<len(frase):
        if frase[i] == letra:
            pos+=1
            if pos == oco:
                return i
            else:
                return -1