def posLetra(string, letra, pos):
    i = 0
    j = 0
    while i < len(string) and j < pos:
        if string[i] == letra:
        	pos +=1
        i+=1
    return i-1