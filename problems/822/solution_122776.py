def repetidos(lista):
    Lista = [1,4,3,3,2,3,3,3,3,5,4,6,6,7,6,8,8,7]
    lista = {i:lista.count(i) for i in lista}
	print lista