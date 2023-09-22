def posLetra(string, letra, pos):
    i = 0
    j = 0
    while i < len(frase) and j < pos:
        if frase[i] == letra:
        	pos +=1
        i+=1
    return i-1