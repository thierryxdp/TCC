def repetidos(lista):
    """Dada uma lista, a função irá retornar quantas vezes
    um elemento é igual ao elemento anterior.
    Tipo da variável lista: list
    Tipo da saída: int"""
    contador = 1
    ocorrencia = 0
    while contador<len(lista):
        if lista[contador] == lista[contador-1]:
            ocorrencia = ocorrencia + 1
		contador = contador + 1
	return ocorrencia