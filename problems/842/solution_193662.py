def pontos_por_time(tabela):
    """recebe uma lista de dois elementos, onde cada um
    desses representa uma lista que contem informacoes
    do numero de gols em dois jogos (ida e volta)
    de futebol entre dois times.
    list->dict"""
    jogo1=tabela[0]
    jogo2=tabela[1]
    casa1=jogo1[0]
    fora1=jogo1[1]
    golsida=jogo1[2]
    golsfora=jogo2[2]
    gols1t1=golsida[0]
    golst2=golsida[1]
    gols2t1=golsfora[0]
    gols2t2=golsfora[1]
    gols1t1=golcasa1
    gols1t2=golfora1
    gols2t1=golcasa2
    gols2t2=golfora2
    pontoscasa=0
    pontosfora=0
    if int(golcasa1)>int(golfora1):
        pontoscasa+=3
    if int(golcasa1)==int(golfora1):
        pontoscasa+=1
        pontosfora+=1
    if int(golcasa1)<int(golfora1):
        pontosfora+=3
    if int(golfora1)>int(golcasa1):
        pontoscasa+=3
    if int(golcasa1)==int(golfora1):
        pontoscasa+=1
        pontosfora+=1
    if int(golfora1)<int(golcasa1):
        pontosfora+=3
    return {casa1:pontoscasa,fora1:pontosfora}