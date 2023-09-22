def uppCons (frase):
    x=0
    FRASE = str.upper(frase)
    while x<=len(frase)-1:
        if FRASE[x] in "AEIOU":
            resposta = str.replace(FRASE, FRASE[x], str.lower(FRASE[x]))
        x=x+1
    return resposta