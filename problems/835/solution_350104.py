def melhor_volta(matriz):
    '''
    Dado uma matriz 6x10 com tempo em s retorna uma tupla 

    Uso:
   melhor_volta(matriz)

    Entrada:
    - matriz (list): Matriz de informação

     Saída:
    - Retorna uma tupla informando quem obteve a melhor volta, seu respectivo tempo e
    em qual volta. (tupla)
    '''
    minimos = []
    for linha in matriz:
        minimos = minimos + [min(linha)]
    menor_tempo = min(minimos)
    corredor = list.index(minimos, menor_tempo)
    volta = list.index(matriz[corredor], menor_tempo)

    return (corredor + 1, menor_tempo, volta + 1)