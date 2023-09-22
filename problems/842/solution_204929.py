def pontos(x):
    gols_1 = x[0]
    gols_2 = x[1]
    if gols_1>gols_2:
        return [3,0]
    if gols_2>gols_1:
        return [0,3]
    if gols_1==gols_2:
        return [1,1]