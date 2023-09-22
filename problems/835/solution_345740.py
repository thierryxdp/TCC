def melhor_volta (matriz):
    """Função que, dada uma matriz 6 x 10 com os tempos em segundos dos corredores em cada volta, retorna uma tupla com o corredor que fez a melhor volta, o tempo e em que volta
    entrada: list
    saída: tuple"""
    
    menor_tempo = 0
    lista_tempo = []
    
    for corredor in matriz:
        for tempo in corredor:
            if tempo == min(corredor):
                lista_tempo = lista_tempo + tempo
        menor_tempo = min(lista_tempo)
        
    return (list.index(lista_tempo,menor_tempo)+1, menor_tempo, list.index(corredor,menor_tempo))