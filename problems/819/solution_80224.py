def filtraMultiplos(lista, n):
    '''Função que recebe uma lista e retorna com números múltiplos do número
    list, int--> list'''    
	multiplo = []  
	contador = 0  
	while contador < len(lista):  
		if lista[contador] % n == 0: 
			multiplo.insert(contador, lista[contador]):
	        contador = contador + 1  
            return multip