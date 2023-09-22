def melhor_volta(matriz):
    """dada uma lista matriz 6x10, na qual as linhas são os pilotos
    e as colunas seus respectivos tempos de volta, retorna uma tupla 
    o nome de quem obteve o melhor tempo de volta e o tempo em segundos,
    e em que volta
    list --> tuple"""
    melhor_tempo=matriz[0][0]
    for piloto in matriz:
        for volta in piloto:
            if volta < melhor_tempo[0]:
                melhor_tempo=[volta]