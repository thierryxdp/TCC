def faltante(lista):
    """Função que dado uma lista contendo N -1 inteiros
    numerados de 1 a N. Retorna o número inteiro que está faltando.list -> int"""
    
    i = 1
    if lista[0] > 1:
        return 1
    while i < len(lista):
        if lista[i] != (i + 1):
        	break
		if lista[i] == (i + 1):
    		i += 1
    return i + 1