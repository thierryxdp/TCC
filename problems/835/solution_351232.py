def melhor_volta(matriz):
    """função que recebe uma matriz como entrada e retorna uma tupla; matriz-->tupla"""
    listaminimos = []
    for m in range(len(matriz)):
        listaminimos = listaminimos + [min(matriz[m])]
    q_tempo = min(listaminimos)
    quemfoi = list.index(listaminimos , q_tempo)
    q_volta = list.index(matriz[quemfoi],q_tempo)
    return (quemfoi + 1, q_tempo,q_volta + 1)