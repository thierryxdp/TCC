def melhor_volta(matriz):
    """
    	Função que retorna de quem foi a melhor volta, com
        qual tempo e em que volta.
        Matriz = 6(corredores) por 10(voltas)
    	list(list) -> tupla
	"""
    pos_i = 0
    pos_j = 0
    elemento = 'ana'
    for i in range(len(matriz)):
        for j in range(i):
            if elemento in matriz[i][j]:
                pos_i = i
                pos_j = j
                break
            break
    return (pos_i,pos_j)