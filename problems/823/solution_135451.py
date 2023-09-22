def faltante(lista):
    caixacompleta= len(lista)+1
    i=1
    pecas=[i]
    while i<caixacompleta:
        pecas+=[(i+1),]
        i=i+1
    	totalpecas= sum(pecas)
    	caixa= sum(len(lista))+1
    	faltando= totalpecas-caixacompleta
    return faltando