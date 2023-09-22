import math
#estou importando math para usar a função math.floor
def bolos(A,B,C):
    #essa função me resultará a quantidade de bolos eu posso obter
    trigo = math.floor(A/2)
    ovo = math.floor(B/3)
    leite = math.floor(C/5)
    #estou dividindo os fatores para obter a quantidade que cada fator pode influênciar em um novo bolo
    if leite <= ovo and leite <= trigo:
        return leite
    if trigo <= leite and trigo <= ovo:
        return trigo
    return ovo