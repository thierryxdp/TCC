def filtraMultiplos(lista,n):
    """Função que ao receber uma lista com números e um número "n",retorna
    todos os elementos da lista original divisíveis por n;
    list, int -> list"""
    listaf = list()
    num_lista = len(lista)
    i = 0
    while(i < num_lista):
        if lista[i]%n == 0:
            listaf += (lista[i],)
		i += 1
	return listaf