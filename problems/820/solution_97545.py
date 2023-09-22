def posLetra(frase,letra,n):
    p=frase.find(letra)
    n=1
    
    while p > 0 and n >=1:
        p=frase.find(letra,p+1)
        
    return p