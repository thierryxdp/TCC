def uppCons(frase):
    x=0
    while x<len(frase):
        if frase[x]!="a"and"e"and"i"and"o"and"u":
            frase=frase[:x]+str.upper(frase[x])+frase[x+1:]
        x=x+1
    return frase