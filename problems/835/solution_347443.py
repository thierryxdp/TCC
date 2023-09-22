def melhor_volta(matriz):
    """ Retorna de quem foi a melhor volta.
    	list -> int
        
        Parameter:
        matriz: Matriz com listas de cada volta de cada corredor.
		
        Returns:
        O número do corredor que teve a melhor volta.
    """
    melhor = []
    for i in matriz:
        melhor.append(min(i))
    return melhor.index(min(melhor)) + 1