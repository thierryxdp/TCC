def pontos_por_time(ida,volta):
    """recebe uma lista de dois elementos, onde cada um
    desses representa uma lista que contem informacoes
    do numero de gols em dois jogos (ida e volta)
    de futebol entre dois times.
    list->dict"""
    casa1=ida[0]
    fora1=ida[1]
    gols1=ida[2]
    gols2=volta[2]
    golcasa1=gols1[0]
    golfora1=gols1[1]
    golcasa2=gols2[1]
    golfora2=gols2[0]
    pontoscasa=0
    pontosfora=0
    if int(golcasa1)>int(golfora1):
        pontoscasa+=3
    if int(golcasa1)==int(golfora1):
        pontoscasa+=1 and pontosfora+=1
    if int(golcasa1)<int(golfora1):
        pontosfora+=3
    if int(golfora2)>int(golcasa2):
        pontoscasa+=3
    if int(golcasa2)==int(golfora2):
        pontoscasa+=1 and pontosfora+=1
    if int(golfora2)<int(golcasa2):
        pontosfora+=3
    return {casa1:pontoscasa,fora1:pontosfora}