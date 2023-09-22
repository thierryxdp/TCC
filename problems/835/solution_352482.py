def melhor_volta(m):
    melhor=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if melhor > m[i][j]:
                melhor = m[i][j]
                pessoa = m[i][j]
                volta = m[j]
    return(pessoa,melhor,volta)