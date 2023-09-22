def filtraMultiplos(lista,n):
    """Retornar uma função que filtre os múltiplos de um n° N, retornando uma nova lista com os divisoras; list,int=>list"""
	lista = []
    i = 0
    while i < len(lista):
    	if lista[i]%n==0:
            lista+=[lista[i],]
    	i=i+1
    return lista