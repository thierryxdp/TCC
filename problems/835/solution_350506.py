def melhor_volta(matriz):
    """Função que recebe uma matriz de entrada que significa os tempos dos corredores em cada volta,
função deve retornar uma tupla com a informação de qual corredor teve a melhor volta, o seu tempo e em qual
volta foi realizada. matriz -> tuple"""
    
    lista_mins=[min(matriz[0]),min(matriz[1]),min(matriz[2]),min(matriz[3]),min(matriz[4]),min(matriz[5])]
    tempo=min(lista_mins)
    corredor=list.index(lista_mins,tempo)
    volta=list.index(matriz[corredor],tempo)
    return (corredor+1,tempo,volta+1)