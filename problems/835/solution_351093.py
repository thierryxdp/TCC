def melhor_volta(m):
    """função q calcula e retorna o vencedor de uma corrida: matriz->tuple"""
    tempos_minimos=[]
    voltas=[]
    for i in range(len(m)):
        tempo=[]
        for j in range(len(m[i])):
            list.append(tempo,m[i][j])
            if len(tempo)==10:
                list.append(tempos_minimos,min(tempo))
                y=list.index(tempo,min(tempo))
                list.append(voltas,y)
    campeao=list.index(tempos_minimos,min(tempos_minimos))+1
    tempo_campeao=min(tempos_minimos)
    volta_campea=voltas[campeao]
    resultado_campeao=[campeao,tempo_campeao,volta_campea]
    return tuple(resultado_campeao)