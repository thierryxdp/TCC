def insere(lista_numero, n):
    """Função que ordene números inteiros incluindo o número
    'n';
    list, int -> list"""
    list.insert(lista_numero, 0, n)
    lista = list.sort(lista_numero)
	return lista