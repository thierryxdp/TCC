def posLetra(frase,letra,num):
    
    i = 0
    c = 0
    if str.count(frase,letra) < num:
        return -1
    else:
        while i<len(frase):
            if c<num and frase[i] == letra:
                c += 1
        i += 1
    return c