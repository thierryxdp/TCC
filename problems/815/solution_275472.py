#dado uma lista de números retorna a mesma lista com o número n adicionado na ordem certa
#list--list
def insere(lista_numero,n):
	list.apeend(lista_numero,n)
	lista_numero.sort()
	return lista_numero