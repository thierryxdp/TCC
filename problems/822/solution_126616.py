def repetidos(lista):
	"""função que conta os numeros repetidos
    list->int"""
    n=1
    repet=0
    while n<len(lista):
        if lista[n]==lista[n-1]:
        	repet=repet+1
        	n=n+1
        else:
            n=n+1
    return repet