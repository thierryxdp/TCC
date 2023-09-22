def posLetra(frase,letra,n):
    i=0
    
    
    while i<len(frase):
        if frase[i]==letra:
             return str.index(frase,letra,n)