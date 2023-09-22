def pontos_por_time(L):
    ''''''
    T1 = L[0][0]
    T2 = L[0][1]
    T1_1 = L[1][1]
    T2_1 = L[1][0]
    pT1 = L[0][2][0]
    pT2 = L[0][2][1]
    pT2_1 = L[1][2][0]
    pT1_1 = L[1][2][1]
    A = 0
    B = 0
    if pT1 > pT2:
        A = A + 3
    if pT1 < pT2:
        B = B + 3
    if pT1 == pT2:
        A = A + 1
        B = B + 1
    if pT1_1 > pT2_1:
        A = A + 3
    if pT1_1 < pT2_1:
        B = B + 3
    if pT1_1 == pT2_1:
        A = A + 1 
        B = B + 1
    return {T1: A, T2: B}