def posLetra(frase,letra,num):
i=0
    contador=0
    while i< len(frase):
        if frase[i] in letra:
            contador  = contador + 1
        i = i + 1
        return contador