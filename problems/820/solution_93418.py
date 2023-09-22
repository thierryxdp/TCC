def posLetra(frase, letra, num):
    x=0
    count=0
    while x<len(frase) and x<num:
        if frase[x]==letra:
            count=count+1
        x=x+1
    if count==num:
        return x-1
    else:
        return -1