def conta_numero(n, m):
    acumulas = 0
    #coluna 
    for j in range(len(m[0])):
        #linha
        for i in range(len(m)):
            if n == [j][i]:
                acumulas = acumulas +1
    return acumulas