def posLetra (frase, x, n):
    palavras = ()  
    palavras = str.index(frase, x,n)
    if palavras >= n:
        palavras =  palavras    
    if palavras < n:
        palavras = -1
   
    return palavras