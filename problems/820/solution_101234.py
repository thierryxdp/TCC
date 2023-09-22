def posletra(frase,letra,n):
    
    i=0
    while i<len(frase):
        if frase[i]==letra:
             return list.index(frase,letra,n)