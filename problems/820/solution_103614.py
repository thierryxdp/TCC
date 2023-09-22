def posLetra(frase, letra, n):
    qt_letras = str.count(frase, letra)
    
    if qt_letras < n:
        return -1
    
    i=0
    c=0
    while i < len(frase):
        if frase[1] == letra:
            c +=1 
        if c == n:
            return i
        i += 1
    return p