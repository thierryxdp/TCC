def melhor_volta(m):
    """função q calcula e retorna o vencedor de uma corrida: matriz->tuple"""
    tempos_minimos=[]#aqui tem o tempo minimo de todos os corredores
    voltas=[]#aqui tem o indice da melhor volta de todos os corredores
    for i in range(len(m)):
        tempo=[]#aqui e uma lista temporaria q uso para verificar o melhor tempo de cada corredor
        for j in range(len(m[i])):
            list.append(tempo,m[i][j])
            if len(tempo)==10:
                list.append(tempos_minimos,min(tempo))
                list.append(voltas,list.index(tempo,min(tempo)))
    campeao=list.index(tempos_minimos,min(tempos_minimos))+1#aqui realizo uma soma de um elemento para assim a posição do campeao se tornar o numero correto pedido na questão (de 1 a 6)
    tempo_campeao=min(tempos_minimos)
    volta_campea=voltas[list.index(tempos_minimos,min(tempos_minimos))]+1#aqui reutilizo o campeao com uma leve diferença para encontrar a volta campea
    resultado_campeao=(campeao,tempo_campeao,volta_campea)
    return resultado_campeao