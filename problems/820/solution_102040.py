def posLetra(frase,x,y):
    i=0
    contador=0
    while i<len(frase) and contador<=y:
        if x==frase[i]:
            contador+=1
        if contador==y:
            return i    
        i+=1

    else:
        return -1