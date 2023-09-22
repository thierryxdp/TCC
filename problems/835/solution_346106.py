def melhor_volta(resultados):
    melhorvolta = []
    for corredor in resultados:
        list.append(melhorvolta,min(corredor))
    x = min(melhorvolta)
    y = list.index(melhorvolta, x)
    z = list.index(resultados[y],x)
    return (y+1,x,z+1)