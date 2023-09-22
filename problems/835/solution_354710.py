def melhor_volta (matriz):
    'função que recebe matriz 6x10, contendo 10 tempos de 6 corredores de kart'
    'e retorna o corredor com o melhor tempo e em que volta. list->tupla'
    inf_corrida=[]
    for n in matriz:
        melhor_tempo=min(n)
        inf_corrida.append(melhor_tempo)
        tempo=min(inf_corrida)
        piloto=inf_corrida.index(tempo)
        volta=matriz[piloto].index(tempo)
    return(piloto+1,tempo,volta+1)