def posLetra(string, letra, numero):
    i = 0
    while i < len(string):
        if string[i] == letra:
            numero -= 1
            if numero == 0:
                return i
        i += 1
        
    return -1