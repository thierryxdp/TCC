def pontos_por_time(lista):
    lista = ['Cormengo', 'Flamínthians', [gc1,gf1]],
    ['Flamínthians','Cormengo',[gc2,gf2]]
    time = {'Cormengo':pontosC, 'Flamínthians':pontosF}
    #jogo 1
    pontosC1 = pontosF1 = 0
    if gc1 > gf1:
        pontosC1 = pontosC + 3
    if gc1 < gf1:
        pontosF1 = pontosF + 3
    if gc1 = gf1:
        pontosF1 = pontosF1 + 1
        pontosC1 = pontosC1 + 1
    #jogo 2
    pontosC2 = pontosF2 = 0
    if gc2 > gf2:
        pontosC2 = pontosC2 + 3
    if gc2 < gf2:
        pontosF1 = pontosF2 + 3
    if gc2 = gf2:
        pontosF2 = pontosF2 + 1
        pontosC2 = pontosC2+ 1
    pontosC = pontosC1 + pontosC2
    pontosF = pontosF1 + PontosF2
    return time