def melhor_volta(resultados):
    '''recebe uma matriz com os tempos dos corredores e retorna uma tupla com a melhor volta da prova, o tempo e em qual volta'''
    '''list(list(int)) -> tuple(int)'''
    melhorvolta = []
    for corredor in resultados:
        list.append(melhorvolta,min(corredor))
    b = min(melhorvolta)
    a = list.index(melhorvolta, b)
    c = list.index(resultados[a],b)
    return (a+1,b,c+1)