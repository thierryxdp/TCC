def posLetra(frase,letra,n):
    i=0
    
    
    while i<len(frase):
         i=i+1
        if frase[i]==letra:
             return  str.index(frase,letra,n)
        elif n < len(qnt):
            return -1