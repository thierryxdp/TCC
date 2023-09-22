def melhor_volta(matriz):
    """Essa função recebe uma lista com os tempos de voltas de um kart e retorna a tupla com o melhor corredor no melhor tempo e a volta com o melhor tempo
    list -> tuple"""
    melhor = []
    for i in range(len(matriz)):
        melhor.append(min(matriz[i]))
    melhor_corredor = melhor.index(min(melhor))+1
    n_volta = (matriz[melhor.index(min(melhor))].index(min(melhor)))+1
    return (melhor_corredor,min(melhor),n_volta)