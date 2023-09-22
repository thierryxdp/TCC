def pontos_por_time(f):

    l1 = f[0]
    l2 = f[1]
#primeira pt

    ponto1 = l1[2]
    
    if ponto1[0]>ponto1[1]:
        t1 = 3
        t2 = 0
    if ponto1[0]==ponto1[1]:
        t1 = 1
        t2 = 1
    if ponto1[0]<ponto1[1]:
        t1 = 0
        t2 = 3

#segunda pt
        
    ponto2 = l2[2]
    
    if ponto2[0]>ponto2[1]:
        t11 = 3
        t22 = 0
    if ponto2[0]==ponto2[1]:
        t11 = 1
        t22 = 1
    if ponto2[0]<ponto2[1]:
        t11 = 0
        t22 = 3

    pontos1 = t1+ t11
    pontos2 = t2+ t22

    fase = {}
    fase[l1[0]] = pontos1
    fase[l2[0]] = pontos2
    return fase