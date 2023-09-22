def melhor_volta(matriz):
    """Função que dada uma lista com os tempos de voltas de kart, retorna uma tupla com o melhor corredor, seu melhor tempo e a volta com o melhor tempo. list -> tuple"""
    melhor = []
    for v in range(len(matriz)):
        melhor.append(min(matriz[v]))
    melhor_corredor = melhor.index(min(melhor))+1
    n_volta = (matriz[melhor.index(min(melhor))].index(min(melhor)))+1
    return (melhor_corredor,min(melhor),n_volta)