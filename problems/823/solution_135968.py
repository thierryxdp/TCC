def faltante(lista):
    """Dada uma lista que simula as peças de um quebra-cabeças,
    a função irá identificar qual peça(número) está faltando. Caso a lista
    esteja supostamente completa, a peça faltante será a do número seguinte
    ao último elemento da lista.
    Tipo da variável lista: list
    Tipo da saída: int"""
    checagem = 1
    contador = 0
    while contador < len(lista):
        if lista[contador] != checagem:
            return checagem
        contador = contador + 1
        checagem = checagem + 1
	return lista[-1]+1