def  faltante (lista):
    """ Dado uma lista de inteiros numerados de 1 até n, retorna qual o valor de n está faltando no intervalo.
    entrada lista inteiro -> sainda int."""
   
    faltante = 0
   
    list.sort(lista)
    tamanho = len(lista)
    
    if lista[0] != 1:
    	faltante = 1
    	return faltante
    
    i = 1
    while i < len(lista):
        if lista[i] != lista[i-1] or lista[i] != [i+1]:
        	faltante = lista[i]
            return faltante
        i = i+1