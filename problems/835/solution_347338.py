##4)Melhor Volta:
def melhor_volta(resultados):
    '''Funcao que recebe uma matriz com os tempos dos corredores e retorna uma
    tupla com a melhor volta da prova, o tempo e em qual volta.
    list(list(int)) -> tuple(int)'''
    melhorV = []
    for corredor in resultados:
        list.append(melhorV,min(corredor))
    b = min(melhorV)
    a = list.index(melhorV, b)
    c = list.index(resultados[a],b)
    return (a+1,b,c+1)