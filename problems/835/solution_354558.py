def melhor_volta(matriz):
    """Função que dada uma matriz 6x10 com os tempos em segundos de 6 corredores,
retorna uma tupla contendo quem teve a melhor volta da prova, list->tuple"""
    melhor_volta=()
    menores_tempos=[]
    corredor=1
    for corredores in matriz:
        menor_tempo=min(corredores)
        menores_tempos.append(menor_tempo)
    for competidores in matriz:
        volta=1
        for tempo in competidores:
            if tempo==min(menores_tempos):
                melhor_volta+=(corredor,tempo,volta)
            volta+=1
        corredor+=1
    return melhor_volta