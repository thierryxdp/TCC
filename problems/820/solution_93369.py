def posLetra(frase,letra,num):
    contador=0
    i = 0 
    somando=0
    while i< len(frase):
        if frase[i] in letra:
            contador = contador + 1
            somando = somando + str.find(frase,letra)
        i=i+1
    return somando