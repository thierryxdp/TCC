import math
def bolos(farinha, ovos, leite):
    ''' '''
    qntd_farinha= farinha//2
    qntd_ovos= ovos//3
    qntd_leite= leite//5
    return min(qntd_farinha, qntd_ovos, qntd_leite)