def faltante(lista):
    i=1
    pecas=[i]
    while n<len(lista)+1:
        pecas+=[(i+1),]
        i+=1
    	totalpecas= sum(pecas)
    	totalfaltante= sum(lista)
   		return totalpecas - totalfaltante