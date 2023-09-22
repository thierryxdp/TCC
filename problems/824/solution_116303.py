def uppCons(frase):
    x=0
    while x<len(frase):
        if frase[x]!="a"and frase[x]!="ã"and frase[x]!="e"and frase[x]!="i"and frase[x]!="o"and frase[x]!="u"and frase[x]!="ú"and frase[x]!="ó"and frase[x]!="í":
            frase=frase[:x]+str.upper(frase[x])+frase[x+1:]
        x=x+1
    return frase