def melhor_volta(matriz:list)->tuple:
    """Dada uma matriz 6x10 com os tempos das 10 voltas de 6 corrredores, retorna uma tupla com quem fez o melhor tempo, em qual volta isso aconteceu e qual foi esse tempo."""
    minimo_corredor=[]
    for corredor in range(1,7):
        list.append(minimo_corredor,min(matriz[corredor-1]))
    menor_tempo=min(minimo_corredor)
    pessoa_melhor_volta=list.index(minimo_corredor,menor_tempo)+1
    volta=list.index(minimo_corredor,menor_tempo)
    return (pessoa_melhor_volta,menor_tempo,volta)