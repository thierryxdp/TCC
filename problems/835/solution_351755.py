def melhor_volta(resultados):
    '''recebe uma matriz com os tempos dos corredores e retorna a melhor volta da prova, o tempo e em qual volta'''
    
    melhor = []
    for corredor in resultados:
        list.append(melhor,min(corredor))
    b = min(melhor)
    a = list.index(melhor, b)
    c = list.index(resultados[a],b)
    return (a+1,b,c+1)