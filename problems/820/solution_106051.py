def posLetra(texto, letra, f):
    i = 0 
    while i< len(texto):
        if texto[i][i] == letra:
            if texto [f] == letra:
                pos = texto.index(texto[f])
            else: 
                pos =-1
        i+=1 
    return pos