def faltante(lista):
    i=1
    pecas=[i]
    while n<len(lista)+1:
        pecas+=[(i+1),]
        i+=1
    total_esperado= sum(pecas)
    total_observado= sum(lista)
   	return total_esperado - total_observado