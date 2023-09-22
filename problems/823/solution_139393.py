def faltante(lista):
    '''retorna a peça faltante de um quebra-cabeça de N peças
    list->int'''
    i=1
    pecas=[i]
    while i<len(lista)+1:
        pecas+=[(i+1),]
        i+=1
    	totalpecas= sum(pecas)
    	totalfaltante= sum(lista)
	return totalpecas-totalfaltante