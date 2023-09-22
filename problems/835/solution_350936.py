def melhor_volta(matriz):
    """
    	Função que retorna de quem foi a melhor volta, com
        qual tempo e em que volta.
        Matriz = 6(corredores) por 10(voltas)
    	list(list) -> tupla
    """
    corredor = 0
    menor_tempo = []
    for voltas in matriz:
        while min(voltas)!=1:
            corredor += 1
    return corredor