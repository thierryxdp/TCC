def pontos_por_time(resultados):
    """calcula o total de pontos de dois times, dados
    seus jogos e gols marcados por cada um.
    list->dict"""
    ida=resultados[0]
    volta=resultados[1]
    
    casa1=ida[0]
    fora1=ida[1]
    
    placar1=ida[2]
    golcasa1=int (placar1[0])
    golfora1=int (placar1[1])
    
    casa2=volta[0]
    fora2=volta[1]
    
    placar2=volta[2]
    golcasa2=int (placar2[0])
    golfora2=int (placar2[1])
    
    decidefora=0
    decidecasa=0
    
    if golcasa1>golfora1:
        decidefora+=3
    if golcasa1==golfora1:
        decidefora+=1
        decidecasa+=1
    if golfora1>golcasa1:
        decidecasa+=3
    if golcasa2>golfora2:
        decidecasa+=3
    if golcasa2==golfora2:
        decidecasa+=1
        decidefora+=1
    if golfora2>golcasa2:
        decidefora+=3
    return {casa1: decidefora, fora1: decidecasa}