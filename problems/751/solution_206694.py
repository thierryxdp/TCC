def quant_palavras(frase):
    i=0
    palavras=1
    while i<len(frase):
        if frase[i] in " ":
            palavras=palavras+1
        i=i+1
    return palavras