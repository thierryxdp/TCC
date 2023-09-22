def faltante(lista):
    n=1
    peca=[]
    while n<=len(lista):
        if (n)!=lista[n-1]:
            peca=lista[n]-1 
        n=n+1
        return peca