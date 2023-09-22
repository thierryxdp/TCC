def melhor_volta(matriz):
    ''' A partir de uma matriz 6x10 no formato de lista com os tempos dos corredores;
retorna uma tupla com o melhor corredor, seu tempo, e em qual volta o fez;
list => tuple'''
    minimos = []
    for corredor in matriz:
        minimos = minimos + [min(corredor)]
    menor = min(minimos)
    ganhou = int(list.index(minimos,menor))+1
    tentativa = int(list.index(matriz[ganhou-1],menor))+1
    return (ganhou,menor,tentativa)