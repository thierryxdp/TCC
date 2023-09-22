def lingua_p(frase):
    vogal="aeiou"
    a=len(frase)
    for i in len(a):
        if str.lower(frase[i]) in vogal:
            frase=list(frase)
            frase[i]=frase[i]+"p"+frase[i]
            frase=''.join(frase)
            i=i+3
        else:
            i=i+1
    return frase