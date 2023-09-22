def faltante(lista):
    i=0
    peca=0
    while i<len(lista):
        if lista[i]==lista[i]:
            peca=peca
        elif lista[i]==lista[i]:
            peca=peca+lista[i]
        elif lista[0]>1:
        	peca=peca+1
        elif lista[-2]<lista[-1]:
            peca=peca+lista[-1]+1
        i=i+1
    return peca