def melhor_volta(matriz):
    lista_temp = []
    lista_volta = []
    for corredor in matriz:
        lista_temp.append(min(corredor))
        lista_volta.append(corredor.index(min(corredor)))
    tempo = min(lista_temp)    
    corredor = lista_temp.index(tempo) + 1
    volta = lista_volta.index(corredor) + 1
    return (corredor, tempo,volta)