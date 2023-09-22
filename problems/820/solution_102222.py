def posLetra(frase,letra,n):
    """
    
    """
    i=0
    repeticoes=""
    while i<len(frase):
        if frase[i]==letra:
            repeticoes+=frase[i]
            i+=1
        if len(repeticoes)==n:             
             return i-1