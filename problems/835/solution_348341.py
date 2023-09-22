def melhor_volta(matriz):
    lista=[]
    CadaCorredor=[]
    for corredor in matriz:
        for tempo in corredor:
            CadaCorredor.append(corredor)
            CadaCorredor.append(min(tempo))
        lista.append(CadaCorredor)
    return lista