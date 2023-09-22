def melhor_volta(matriz):
    """ Retorna de quem foi a melhor volta.
    	list -> tuple
        
        Parameter:
        matriz: Matriz com listas de cada volta de cada corredor.
		
        Returns:
        O número do corredor que teve a melhor volta.
    """
    tempo = []
    volta = []
    for i in matriz:
        tempo.append(min(i))
        volta.append(index(min(i)) + 1)
    return (tempo.index(min(tempo)) + 1, min(melhor), volta.index(min(volta)) + 1)