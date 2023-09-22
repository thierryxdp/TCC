def posLetra(frase, x, n):
    palavras = ()
    i=0
    palavras = str.index(frase, x,n)
    while i>len (frase):
        
        if palavras >= n:
            palavras =  palavras    
        if palavras < n:
            palavras = -1
        if x not in palavras:
            palavras = -1
    i=i+1
    return palavras