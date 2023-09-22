def insere(lista_numero,n):
	'''recebe uma lista com numeros crescentes e um numero inteiro n, retornando uma lista
    com n incluso em posição ordenada'''
    nova_lista = lista_numero + n
    list.sort(nova_lista)
    
    return nova_lista