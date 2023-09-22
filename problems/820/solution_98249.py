def posLetra(frase, letra, n):
    i = 0
    frase_l = list(frase)
    count = 0
    returned = False
    
    while i < len(frase_l):
        if frase_l[i] == letra:
            count += 1
        if count == n:
            return i
        	returned = True
        i += 1
    
    if returned == False:
        return -1