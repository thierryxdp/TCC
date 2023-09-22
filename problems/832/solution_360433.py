def eh_quadrada(P):
    if P[0]==[]:
        return True
    acumulaC=len(P[0])
    acumulaL=len(P)
    '''for i in P:
        acumulaL+=1
        for j in i:
            acumulaC+=1'''
    if acumulaL == acumulaC:
        return True
    else:
        return False