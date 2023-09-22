def insere(lista_numero,n):
    '''Função que, dada uma lista cresente e um número inteiro, retorna
    	a lista com o número inserido no local correto, onde a ordem
        crescente permaneça coerente
        
        list, int -> list
    	'''
    lista_numero = lista_numero + [n]
    list.sort(lista_numero)
    return lista_numero