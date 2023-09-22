def melhor_volta (matriz):
    """Função que, dada uma matriz 6 x 10 com os tempos em segundos dos corredores em cada volta, retorna uma tupla com o corredor que teve a melhorvolta, seu tempo e em que volta
    entrada: list
    saída: tuple"""
    
    lista_tempos = []
    
    for corredor in matriz:
        list.append(lista_tempos, min(corredor))
        volta = list.index(corredor, min(corredor))
        if min(corredor) == min(lista_tempos):
            atleta = list.index(matriz,corredor) + 1
            
    return (atleta, min(lista_tempos), volta)