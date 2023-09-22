def melhor_volta(matriz):
    converteTempo = []
    contaVoltas = 0
    for tempo in matriz:
        for minuto in tempo:
            converteTempo = min([minuto])
            contaVoltas+=1    
    return contaVoltas