def pontos_por_time(x):
    j1 = x[0]
    j2 = x[1]
    p1 = j1[2]
    p2 = j2[2]
    p_cor = 0
    p_fla = 0
    if p1[0] > p1[1]:
        p_cor += 3
    if p1[0] < p1[1]:
        p_fla += 3
    if p1[0] == p1[1]:
        p_cor += 1
        p_fla += 1
    if p2[0] > p2[1]:
        p_fla += 3
    if p2[0] < p2[1]:
        p_cor += 3
    if p2[0] == p2[1]:
        p_cor += 1
        p_fla += 1
    if p_cor > p_fla:
        return ['Cormengo', p_cor]
    else:
        return ['Flamínthians', p_fla]