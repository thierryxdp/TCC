def pontos_por_time(jogo):
    """  [[’Cormengo’,’Flaminthians’, [1, 0]], primeiro jogo
    [’Flamınthians’, ’Cormengo’, [2, 2]]] segundo jogo
    """
    jogo1=jogo[0]
    jogo2=jogo[1]
    t1=jogo1[0]
    t2=jogo1[1]
    t1==jogo2[2]
    t2==jogo2[1]
    P1=jogo1[2]
    p2=jogo2[2]
    
    r1=()
    r2=()

    #Primeiro jogo
    if p1[0] > p1[1]:
        return r1()= 3
    elif p1[0]==p1[1]:
        return r1 += 1
               r2 += 1
    elif p1[0] < p2[1]:
        return r2 += 3
    #Segundo jogo
    r11={}
    r22={}
    if p2[0]>p2[1]:
        return r22 += 3
    elif p2[0]=p2[1]:
        return r11 += 1
               r22 += 1
    elif p2[0]<p2[1]:
        return r11=3
    #Placar:
    ponto1= r1+r11
    ponto2= r2+r22
    
    return {t1, ':', ponto1,',', t2, ':', ponto2}