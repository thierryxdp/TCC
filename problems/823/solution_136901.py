def faltante (lista):
    '''Função que dada uma lista 'lista' de entrada 
    retorna o valor do item falt
    list(int) -> int'''
    indice=0
    contador=0
	if lista[0]!=1:
        return 1
	while cont<len(lista)-1:
        if lista[ind]+1==lista[ind+1]:
            ind=ind+1
            cont=cont+1
    	else:
        	contador=len(lista)
	return lista[ind]+1