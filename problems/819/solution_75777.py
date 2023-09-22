def filtraMultiplos(lista,n):
	"""Retorna os elementos da lista que são múltiplos de n.
Parametros:
Entrada:list
Saida:int"""
    lista_div=[]
    proximo=0
    while proximo<len(lista):
   		if lista[proximo]%n==0:
            lista_div.append(lista[proximo]) 
       	proximo=proximo+1
    return lista_div