def faltante(lista):
    lista_o=lista[:]
    tam= len(lista)
    lista = range(1, tam)
    peca=[]
    i=0
    
    while i<len(lista_o):
        if lista[i] in lista_o:
            peca=pec+[]
        else:
            peca=peca+[lista[i]]
            
    return peca