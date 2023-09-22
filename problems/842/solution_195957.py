def pontos_por_time(lista):
    jogo1 = lista[0]
    jogo2 = lista[1]
    nometime1=jogo1[0]
    nometime2 = jogo2[0]
    placar1=jogo1[1]
    placar2 = jogo2[1]
    if placar1[0]>placar1[1]:
        m1= 3
        v1=0
    elif placar1[0]==placar1[1]:
        m1=1
        v1=1
    else:
        m1=3
        v1=0
        
    if placar2[0]>placar2[1]:
        m2= 3
        v2=0
    elif placar2[0]==placar2[1]:
        m2=1
        v2=1
    else:
        m2=3
        v2=0
     
    if m1+v2 > m2 +v1:
    dicionario ={nometime1:m1+v2,nometime2:m2+v1}
    return dicionario
    elif m1 +v2 == m2+v1:
    dicionario ={nometime1:m1+v2,nometime2:m2+v1}
    return dicionario
    else:
        dicionario ={nometime2:m2+v1,nometime1:m1+v2}
    return dicionario