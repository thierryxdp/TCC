def uppCons(frase:str)->str:
    x=0
    while x<len(frase):
        if frase[x] in not "aeiou":      
            str.upper(frase[x])
        x=x+1
    return frase