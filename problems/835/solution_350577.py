def melhor_volta(M):
    volta = 0
    tempo = 0
    corredor = 0
    tempos = []
    for a in M:
        for b in a:
            tempos = tempos + [b]
    for a in M:
        for b in a:
            if b == min(tempos):
                corredor = corredor + M.index(a) + 1
                tempo = tempo + b
                volta = M[M.index(a)].index(b) + 1
                
    return (corredor,tempo,volta)