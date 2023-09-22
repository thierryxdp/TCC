#dado uma lista de números retorna a mesma lista com o número n adicionado na ordem certa
#list--list
def insere(lista_numero,n):
	y=list.append(lista_numero, n)
	z=list.sort(y)
	return z