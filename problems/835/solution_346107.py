def melhor_volta(resultados):
    '''Retorna uma tupla informando de quem foi a melhor volta da prova, com qual tempo e em qual volta. Baseia-se na matriz 6x10 do enunciado.
    list -> tuple'''
    melhorvolta = []
    for corredor in resultados:
        list.append(melhorvolta,min(corredor))
    x = min(melhorvolta)
    y = list.index(melhorvolta, x)
    z = list.index(resultados[y],x)
    return (y+1,x,z+1)