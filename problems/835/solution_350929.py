def melhor_volta(matriz):
    """
    	Função que retorna de quem foi a melhor volta, com
        qual tempo e em que volta.
        Matriz = 6(corredores) por 10(voltas)
    	list(list) -> tupla
    """
    for voltas in matriz:
        return min(voltas)