#dado uma lista de números crescente retorna a mesma lista com o número n adicionado na ordem certa
#list--list
def insere(lista_numero,n):
	lista_numero=list.append(lista_numero, n)
	lista_numero=list.sort(lista_numero)
	return lista_numero