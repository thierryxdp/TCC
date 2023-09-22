def melhor_volta(matriz):
    """
    	Função que retorna de quem foi a melhor volta, com
        qual tempo e em que volta.
        Matriz = 6(corredores) por 10(voltas)
    	list(list) -> tupla
    """
    menor_tempo = []
    for voltas in matriz:
        menor_tempo.append(min(voltas))
    menor_tempo = min(menor_tempo)  
    
    corredor = 0
    for voltas in matriz:
        while menor_tempo not in voltas:
            corredor += 1

    return (corredor,menor_tempo)