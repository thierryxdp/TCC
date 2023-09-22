def melhor_volta(m):
    volta= len(m[0])
    pessoa = len(m)
    melhor_da_vez=m[0][0]
    for i in range(volta):
        for j in range(pessoa):
            if m[i][j]< melhor_da_vez:
                pessoa = i
                volta=j
                tempo=m[i][j]
                melhor_da_vez=m[i][j]
    return (pessoa,tempo,volta)