def insere(lista_numero, n):
    """dada uma lista de numeros em ordem crescente e um numero n, a função inclui n na lista, manten
    do a sua ordenação; list, int -> list"""
    
	lista_completa = lista_numero + [n]
    listanova = list.sort(lista_completa)
    return listanova