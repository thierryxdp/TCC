def eh_quadrada(matriz):
    """funcao que retorna se uma determindada matriz e quadrada;
    list->bolleano"""
    if matriz==[]:
        return True
	elif len(matriz)==len(matriz[0]):
		return True
    else:
        return False