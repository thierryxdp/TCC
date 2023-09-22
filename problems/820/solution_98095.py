def posLetra(frase,letra,num):
    """..."""
    pos = 0
    contador = 0
    i = 0
    while i<len(frase):
        if frase.count(letra) < num:
            pos = -1
        else:
            contador +=1