def melhor_volta(matriz):
    LT = []; LC = []
    for i in matriz:
        x = min(i)
        y = i.index(x)
        LT.append(x)
        LC.append(y)
	MT = min(LT); MV = LT.index(MT); MC = LC[MV]
    return (MV +1, MT, MC +1)