def posLetra(x,y,z):
    i=0
    contador_pos=[]
    while i < len(x):
        if x[i] == y:
            contador_pos = contador_pos + [i]
        i = i + 1
    if len(contador_pos) >= z :
        return contador_pos[z-1]
    else:
        return -1