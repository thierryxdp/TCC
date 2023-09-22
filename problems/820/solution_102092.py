def posLetra(frase, x, n):
    palavras = ()  
    i=0
    i=i+1
    palavras = str.count(frase, x)
    if palavras >= n:
        palavras =  palavras    
    else:
        palavras = -1
    
    return palavras