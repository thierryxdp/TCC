def melhor_volta(matriz):
    ''' Função que dada uma matriz contendo sublistas com
    o tempo de percurso de 6 corredores em cada volta, no
    total de 10 voltas, retorna uma tupla contendo de quem 
    foi o percurso mais rápido, em qual tempo e em que volta.
    Entrada: list
    Retorno: tuple '''

    resultados = []

    for i in range(len(matriz)):
        corredor = i + 1
        menor_tempo = min(matriz[i])
        volta = list.index(matriz[i],menor_tempo) + 1
        resultados = resultados + [[corredor,menor_tempo,volta]]

    menores_tempos = []
    for corredor in resultados:
        list.append(menores_tempos,corredor[1])
    menor = min(menores_tempos)
    indice = list.index(menores_tempos,menor)

    return tuple(resultados[indice])