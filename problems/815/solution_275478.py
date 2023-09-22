#dado uma lista de números retorna a mesma lista com o número n adicionado na ordem certa
#list--list
def insere(x,n):
	x=list.appeend(x, n)
	x=list.sort(x)
	return x