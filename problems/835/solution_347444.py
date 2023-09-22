def melhor_volta(matriz):
    """ Retorna de quem foi a melhor volta.
    	list -> tuple
        
        Parameter:
        matriz: Matriz com listas de cada volta de cada corredor.
		
        Returns:
        O número do corredor que teve a melhor volta.
    """
    melhor = []
    for i in matriz:
        melhor.append(min(i))
    return (melhor.index(min(melhor)) + 1, min(melhor), i.index(min(i)))