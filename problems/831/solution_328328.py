def lingua_p(frase):
    vogal="aeiou"
    i=len(frase)
    a=0
    for a in range(i):
        if str.lower(frase[i]) in vogal:
            frase=list(frase)
            frase[i]=frase[i]+"p"+frase[i]
            frase=str.join(frase,"")
    return