def faltante(lista):
    n=1
    peca=[]
    while n<=len(lista)+1:
        if n not in lista:
            peca=n  
        n=n+1
    return peca