def uppCons(frase):
    x=0
    while x<len(frase):
        if frase[x]!="a":
            frase=frase[:x]+str.upper(frase[x])
        x=x+1
    return frase