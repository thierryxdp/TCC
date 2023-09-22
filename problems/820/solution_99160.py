def posLetra(string, letra, pos):
    i = 0
    j = 0
    while i < len(string) and j < pos:
        if string[i] == letra:
        	j+=1
        i+=1
    if j < pos:
        return -1
    else:
    	return i-1