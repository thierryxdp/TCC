def eh_quadrada(P):
    acumulaC=0
    acumulaL=0
    for i in P:
        acumulaL+=1
        for j in i:
            acumulaC+=1
    if acumulaL == acumulaC:
        return True
    else:
        return False