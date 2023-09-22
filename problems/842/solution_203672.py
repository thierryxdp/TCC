def pontos_por_time(lista):
    jogo1=lista[0]
    jogo2=lista[1]
    pontos1=jogo1[2]
    pontos2=jogo2[2]
    t1j1=pontos1[0]
    t1j2=pontos2[1]
    t2j1=pontos1[1]
    t2j2=pontos2[0]
    if t1j1==t2j1:
        a1=1
        b1=a1
    if t1j1<t2j1:
        a1=0
        b1=3
    if t1j1>t2j1:
        a1=3
        b1=0
    if t1j2==t2j2:
        a2=1
        b2=a2
    if t1j2<t2j2:
        a2=0
        b2=3
    if t1j2>t2j2:
        a2=3
        b2=0
    dicio={}
    list(dict.keys(dicio))=[jogo1[0],jogo2[1]]
    list(dict.values(dicio))=[t1j1*a1+t1j2*a2,t2j1*b1+t2j2*b2]
    return dicio