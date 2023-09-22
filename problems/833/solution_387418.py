def conta_numero(n, m):
    acumulas = 0
    #coluna 
    for i in range(len(m)):
        #linha
        for j in range(len(m[0])):
            if n == [j][i]:
                acumulas = acumulas +1
    return acumulas