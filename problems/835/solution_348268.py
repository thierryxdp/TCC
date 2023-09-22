def melhor_volta(matriz):
    """função que dada uma matriz 6x10 com os tempos dos corredores, retorna de quem foi a melhor volta, em qual tempo e em que volta;list-->tuple"""
    tempo=150
    for x in range(6):
        if min(matriz[x])<tempo:
            tempo=min(matriz[x])
            melhorVolta=matriz[x].index(tempo)+1
            corredor=x+1
    return corredor,tempo, melhorVolta