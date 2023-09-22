def melhor_volta(matriz):
    """Retorna uma tupla informando quem teve a melhor volta,em qual tempo e em que volta.list-->tuple"""
    minimos=[]
    val_minimo=0
    for i in range(len(matriz)):
        minimos=minimos+[min(matriz[i])]
    val_minimo=val_minimo+min(minimos)
    for z in range(len(matriz)):
        if val_minimo in matriz[z]:
            return z,val_minimo