def melhor_volta(resultados):
    '''Função que recebe uma matriz com os tempos dos corredores
    e retorna uma tupla informando de quem foi a melhor volta da
    prova, com qual tempo e em qual volta.
    list -> tuple'''
    
    MelhorVolta = []
    
    for corredor in resultados:
        list.append(MelhorVolta,min(corredor))
    
    b = min(MelhorVolta)
    a = list.index(MelhorVolta, b)
    c = list.index(resultados[a],b)
    
    return (a+1,b,c+1)