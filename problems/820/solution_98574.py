def posLetra(frase,x,y):
    i = 0
    contador = 0
    while contador < y:
        if frase[i] == x: 
           contador = contador + 1
           i = i + 1
        elif frase[i] != x:
            i = i + 1
    return i