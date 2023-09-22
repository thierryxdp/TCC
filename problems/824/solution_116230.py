def uppCons(frase:str)->str:
    x=0
    while x<len(frase):
        if frase[x]!="aeiouAEIOU":
            str.upper(frase[x])
            
    return frase