def melhor_volta(matriz):
    lista=[]
    for corredor in matriz:
        for tempo in corredor:
            lista.append(corredor,min(tempo))
    return lista