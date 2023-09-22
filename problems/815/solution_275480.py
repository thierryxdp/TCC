#dado uma lista de números retorna a mesma lista com o número n adicionado na ordem certa
#list--list
def insere(x,n):
	y=list.append(x, n)
	z=list.sort(y)
	return z