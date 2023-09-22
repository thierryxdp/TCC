def posLetra(frase, letra, num):
    x=0
    count=0
    while x<=len(frase)-1:
        if frase[num]==letra:
            count=count+1
        x=x+1
    return count