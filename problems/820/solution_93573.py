def posLetra(frase,letra,num):
    frase1 = frase
    contador=0
    i = 0 
    somando=0
    while i< len(frase):
        if frase[i] in letra:
            contador = contador + 1
            somando = somando + str.find(frase1,letra)
        i=i+1
        
    return somando