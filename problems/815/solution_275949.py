def insere(lista_numero,n):
    '''funçao que recebe uma lista ordenada(crescente) de numeros inteiros e um numero inteiro n,
    inclui n na posiçao certa
    list,int-->list,int'''
		listaInsere= lista_numero +[n]
		list.sort(listaInsere)
    	return listaInsere