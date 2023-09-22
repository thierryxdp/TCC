def faltante(lista):
    l=lista[:]
    l.sort()
    contador=0
    peca=-1
    while contador <len(l):
        if l[contador]==contador+1:
            contador+=1
        else:
            peca=contador+1
            contador=1
            
    if peca==-1:
            peca=len(l)+1
        
    return peca