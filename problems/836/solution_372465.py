def ordena_por_insercao(lista):
    '''função que recebe uma lista e retorna ela ordenada por inserção
    entrada:list
    saida:list'''
    contador=[]
    i=0
    while i<len(lista):
        elementoMin=min(lista)
        contador=contador+[elementoMin]
        list.remove(lista,elementoMin)
	return contador