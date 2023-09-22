def melhor_volta(matriz):
    converteTempo = []
    for tempo in matriz:
        for minuto in tempo:
            converteTempo += min([minuto/60])
    return converteTempo