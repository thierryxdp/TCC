def posLetra(frase, x, n):
    palavras = ()  
    i=0
    palavras = str.index(frase, x)
    if palavras >= n:
        palavras =  palavras    
    else:
        palavras = -1
    i=i+1
    return palavras