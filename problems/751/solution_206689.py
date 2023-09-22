def quant_palavras(frase):
    i=0
    palavras=0
    while i<len(frase):
        if " ":
            palavras=palavras+1
            i=i+1
    return palavras