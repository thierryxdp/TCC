def intercala(lista1, lista2):
    """Lista 1 é intercalada com Lista 2 e cria a lista 3"""
    lista3=lista1*2
	lista3[1::2]=lista1
	lista3[::2]=lista2