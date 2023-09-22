def melhor_volta(matriz):
    converteTempo = []
    for tempo in matriz:
        for minuto in tempo:
            converteTempo += [minuto/60]
    return min(converteTempo)