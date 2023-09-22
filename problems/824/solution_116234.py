def uppCons(frase:str)->str:
    x=0
    str.split(frase)
    while x<len(frase):
        if frase[x]!="aeiou":
            str.upper(frase[x])
        x=x+1
    return frase