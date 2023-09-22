def insere(lista_numero, n):
    """dada uma lista de numeros em ordem crescente e um numero n, a função inclui n na lista, manten
    do a sua ordenação. Para isso, a função cria uma lista nova ''lista_completa'' que é composta da lista original
    e o novo elemento n. Então, através do list.sort, retorna-se essa lista_completa ordenada; 
    list, int -> list"""
    
	lista_completa = lista_numero + [n]
    list.sort(lista_completa)
    return lista_completa