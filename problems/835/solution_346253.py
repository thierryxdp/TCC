def melhor_volta(lista_tempos:list) -> tuple:
    """Função que irá receber uma matriz 6x10 que irá conter os tempos em segundos dos 6 corredores em cada uma das 10 voltas. A função irá retornar uma tupla informando quem fez a melhor volta da prova, qual foi o tempo em segundos em que essa volta foi feita e qual foi essa volta.
        list -> tuple
    
        Parameters:
        tempos: lista que representa uma matriz 6x10

        Returns:
        tupla tupla informando de quem fez a melhor volta da prova, qual foi o tempo em segundos em que essa volta foi feita e qual foi essa volta.
    """

    acumulador = []
    menor_tempo = 1000
    volta = 0
    corredor = 0
    for corredores in range(len(lista_tempos)):
        for tempo_por_volta in range(len(lista_tempos[0])):
            if lista_tempos[corredores][tempo_por_volta] < menor_tempo:
                menor_tempo = lista_tempos[corredores][tempo_por_volta]
                volta = tempo_por_volta + 1
                corredor = corredores + 1
    return corredor, menor_tempo, volta