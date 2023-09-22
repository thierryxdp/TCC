def repetidos(lista_de_numeros):
    """retorna quantas vezes temos os numeros anteriores 
    iguais"""
    passador = 0
    contador = 0
    while passador < len(lista_de_numeros):
        if lista_de_numeros[passador] == lista_de_numeros[passador + 1]:
            contador = contador + 1
            passador += 1
	return contador