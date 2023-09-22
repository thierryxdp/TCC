def lingua_p(frase):
    vogal="aeiou"
    a=len(frase)
    for i in range(a):
        if vogal in str.lower(frase):
            frase=list(frase)
            frase[i]=frase[i]+"p"+frase[i]
            frase=''.join(frase)
    return frase