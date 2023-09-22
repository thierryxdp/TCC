def posLetra(frase, letra, num):
    x=0
    count=0
    while x<=len(frase)-1:
        if letra==frase[x]:
            count=count+1
        x=x+1
    return x