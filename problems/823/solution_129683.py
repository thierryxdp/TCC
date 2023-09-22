def faltante(lista):
    n=0
    peca=[]
    while n<len(lista):
        if (n+1)!=lista[n]:
            peca=lista[n]+1    
        n=n+1
        return peca