def pontos_por_time(lista):
    jogo1 = lista[0]
    jogo2 = lista[1]
    nome_t1 = jogo1[0]
    nome_t2= jogo2[0]
    pontostotal1 = 0
    pontostotal2 = 0
    if(jogo1[2][0] > jogo1[2][1]):
        pontostotal1 += 3
   	if(jogo1[2][0] < jogo1[2][1]):
        pontostotal2 += 3
    pontostotal1 = pontosj1t1 + pontosj2t1
    pontostotal2 = pontosj1t2 + pontosj2t2
    return {nome_t1:pontostotal1, nome_t2:pontostotal2