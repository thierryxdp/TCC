def melhor_volta(m):
    lista = []
    for corredor in m:
        tempo = min(corredor)
        list.append(lista,tempo)
    
    melhorTempo = min(lista)
    melhorCorredor = 1 + list.index(lista,melhorTempo)
    i = 0
    
    for corredor in m[i]:
        if melhorTempo == corredor:
            numVolta = i
        i = i + 1
        
    return (melhorCorredor, melhorTempo, numVolta)