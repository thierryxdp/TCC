def posLetra(frase,l,n):
    i=0
    contador=0
    for i in list(range(0:len(frase))):
        if frase[i]==l:
            contador=contador+1
    elif contador==n:
        return i