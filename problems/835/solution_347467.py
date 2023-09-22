def melhor_volta(matriz):
    converteTempo = []
    for tempo in matriz:
        for minuto in tempo:
            converteTempo += round([minuto/60],2)
    return converteTempo