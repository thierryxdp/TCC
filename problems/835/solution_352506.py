def melhor_volta(m):
    volta= len(m[0])
    pessoa = len(m)
    for i in range(pessoa):
        for j in range(volta):
            if m[i][j]< m[0][0]:
                pessoa = i
                volta=j
                tempo=m[i][j]
    return (pessoa,tempo,volta)