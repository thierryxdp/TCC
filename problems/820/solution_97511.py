def posLetra(frase,letra,n):
    p=frase.find(letra)
    
    while.p>0 and n > 1:
        p=frase.find(letra,p+1)
        n-=1
        
    return p