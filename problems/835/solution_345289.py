def melhor_volta(matriz:list)->tuple:
    """Dada uma matriz 6x10 com os tempos das 10 voltas de 6 corrredores, retorna uma tupla com quem fez o melhor tempo, em qual volta isso aconteceu e qual foi esse tempo."""
    minimo_corredor=[]
    minimo_total=[]
    for corredor in range(1,7):
        list.append(minimo_corredor,min(matriz[corredor-1]))
    list.append(minimo_total,minimo_corredor)
    menor_tempo=min(minimo_corredor)
    menor_tempo_total=min(minimo_total)
    pessoa_melhor_volta=list.index(minimo_total,menor_tempo)
    volta=list.index(matriz,menor_tempo)
    return (pessoa_melhor_volta,volta,menor_tempo_total)