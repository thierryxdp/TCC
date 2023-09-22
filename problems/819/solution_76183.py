def filtraMultiplos(lista,num):
    """Dada uma lista de numeros e um numero como segundo parametro, deve retornar uma nova lista apenas com os numeros da lista original que sao multiplos do numero no segundo parametro"""
    """entrada: lista,int
    saida: lista"""
    
    
    lista_multiplos = []
    pos = 0
    
    while pos < len(lista):
        if  lista[pos] % num ==0:
        	list.append(lista_multiplos,lista[pos])
    	pos = pos +1
    
    return lista_multiplos