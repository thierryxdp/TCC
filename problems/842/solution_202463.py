def pontos_por_time(L1):
    """A função recebe os times e o placar do jogo entre eles em formato de lista. Por conseguinte, retornna uma lista com o nome do time e os pontos adquiridos na rodada"""
    L2 = L1[0]
    L3 = L1[1]
    L4 = L2[2]
    L5 = L3[2]
    L6 = L4[0]
    L7 = L4[1]
    L8 = L5[0]
    L9 = L5[1]
    L10 = L2[0]
    L11 = L2[1]
    if L6>L7:
        var1 = 3; var3 = 0
    elif L6 == L7:
        var1 = 1; var3 = 1
    elif L6<L7:
        var1 = 0; var3 = 3
    if L8>L9:
        var2 = 0; var4 = 3
    elif L8 == L9:
        var2 = 1; var4 = 1
    elif L8<L9:
        var2 = 3; var4 = 0
    return {L10:(var1 + var2),L11:(var3 + var4)}
#Start your python function here