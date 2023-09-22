def carros (pessoas, capacidade=5):
    q=pessoas//capacidade
    r=pessoas%capacidade
    carros= q+ round(r+0.5)
    return carros