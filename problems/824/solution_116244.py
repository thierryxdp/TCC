def uppCons(frase:str)->str:
    x=0
    frase=frase.split()
    while x<len(frase):
        if "aeiou" in frase[x]:
            str.upper(frase[x])
        x=x+1
    return frase