def posLetra(frase, x, n):
    palavras = ()  
    i=0 
    i=i+1
    palavras = str.index(frase, x,n)
    if palavras >= n:
        palavras =  palavras    
    if palavras < n:
        palavras = -1
   
    return palavras