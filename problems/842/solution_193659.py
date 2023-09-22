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
    gols1=jogo1[2]
    gols2=jogo2[2]
    golcasa1=gols1[0]
    golfora1=gols1[1]
    golcasa2=gols2[1]
    golfora2=gols2[0]
    pontoscasa=0
    pontosfora=0
    if int(golcasa1)>int(golfora1):
        pontoscasa+=3
    if int(golcasa1)==int(golfora1):
        pontoscasa+=1
        pontosfora+=1
    if int(golcasa1)<int(golfora1):
        pontosfora+=3
    if int(golfora1)>int(golcasa=1):
        pontoscasa+=3
    if int(golcasa1)==int(golfora1):
        pontoscasa+=1
        pontosfora+=1
    if int(golcasa1)<int(golfora1):
        pontosfora+=3
    return {casa1:pontoscasa,fora1:pontosfora}