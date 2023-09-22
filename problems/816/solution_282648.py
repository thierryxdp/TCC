def maiores(lista_numero,n):
    maiores=[item for item in lista_numero if item > n]
	return sorted(maiores)
'''dado um numero e uma lista retorna uma nova lista com os numeros maiores
que ele
list,int->list'''