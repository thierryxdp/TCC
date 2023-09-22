def melhor_volta(m):
    melhor = 100
    pessoa=0
    volta=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if  m[i][j]< melhor :
                melhor= m[i][j]
                pessoa = m[i]
                volta= i
    return(pessoa,melhor,volta)