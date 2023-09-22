#dado uma lista de números retorna a mesma lista com o número n adicionado na ordem certa
#list--list
def insere(lista_numero,n):
	x=lista_numero
	list.apeend(x,n)
	lista_numero.sort()
	return lista_numero