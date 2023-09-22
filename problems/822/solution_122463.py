def repetidos(lista):
    qtd=0
    for x in lista:
        if x<len(lista):
        	if lista[x+1]==x:
            	qtd+=1
    return qtd