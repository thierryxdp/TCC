def melhor_volta(matriz):
    converteTempo = []
    contaVoltas = 0
    for tempo in matriz:
        contaVoltas+=1
        for minuto in tempo:
            converteTempo = min([minuto])
    return contaVoltas