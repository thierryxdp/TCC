def repetidos(lista):
    """Retorna o número de vezes que um elemento da lista é igual ao elemento anterior.
    Parametros:
    Entrada:list
    Saida:int"""
	contador=0
    acumulador=0
    while contador<len(lista)-1:
    	if lista[contador+1]==lista[contador]:
        	acumulador=acumulador+1
        contador=contador+1
    return acumulador