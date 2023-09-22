def filtraMultiplos(numeros,n):
    '''Função recebe uma lista de numeros como entrada e retorna outra lista com os múltiplos do mesmo.
    	lista,int -> lista'''
    	
	ListaNumeros = []
    indice = 0 
    TamanhoLista = len(numeros)
    
    while indice < TamanhoLista:
        if numeros[indice] % n == 0:
            ListaNumeros.append(numeros[indice])
		indice = indice + 1
	return ListaNumeros