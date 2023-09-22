def faltante(lista):
    lista_o=lista[:]
    tam= len(lista)
    lista = range(1, tam)
    peca=[]
    i=0
    
    while i<len(lista_o):
        
        if lista[i] in lista_o:
            peca=peca+[lista[i]]
            
        i = i + 1
            
    return peca