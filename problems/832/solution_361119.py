def eh_quadrada(matriz):
    """Função que retorna se uma função é quadrada ou não. Entrada: Lista. Saida: strig"""
    nlin = len(matriz)
    ncol = len(matriz[0])
    if nlin > ncol:
        print ('False')
    if nlin < ncol:
        print ('False')
    elif nlin == ncol:
    	print ('True')