def  faltante (lista):
    """ Dado uma lista de inteiros numerados de 1 até n, retorna qual o valor de n está faltando no intervalo.
    entrada lista inteiro -> sainda int."""
   
    faltante = 0
   
    list.sort(lista)
    tamanho = len(lista)
   
    i = 1
    while i < tamanho:
        if lista[0] != 1:
            faltante = 1
        	return faltante
        if not (lista[i] == lista[i-1]) or not(lista[i] == lista[i+1]):
        	faltante = lista[i]
        	return faltante
		
        
		i = i+1