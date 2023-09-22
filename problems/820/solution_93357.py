def posLetra(frase,letra,num):
    contador=0
    i = 0 
    somando=0
    while i< len(frase):
        if frase[i] == letra:
            somando = somando + i
        i=i+1
    return i