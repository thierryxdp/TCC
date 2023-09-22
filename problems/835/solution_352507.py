def melhor_volta(m):
    volta= len(m[0])
    pessoa = len(m)
    melhor_da_vez=m[0][0]
    for i in range(pessoa):
        for j in range(volta):
            if m[i][j]< melhor_da_vez:
                pessoa = i
                volta=j
                tempo=m[i][j]
                melhor_da_vez= tempo
    return (pessoa,tempo,volta)