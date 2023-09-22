def pontos(l1):
    l=()
    gc=0
    gf=0
    if l1[0][2][0] == l1[0][2][1]:
        gc = gc+1
        gf = gf+1
    elif l1[0][2][0] > l1[0][2][1]:
        gc = gc+3
    else:
        gf = gf+3
    if l1[1][2][0] == l1[1][2][1]:
        gc = gc+1
        gf = gf+1
    elif l1[1][2][0] > l1[1][2][1]:
        gf = gf+3
    else:
        gc = gc+3
    flaminthians= {l1[0][1]: gf}
    cormengo= {l1[0][0]: gc}
    return cormengo