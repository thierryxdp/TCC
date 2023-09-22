import math
def bolo(farinha, ovo, leite):
    ''' '''
    qntd_farinha = farinha//2
    qntd_ovo = ovo//3
    qntd_leite = leite//5
    return min(qntd_farinha, qntd_ovo, qntd_leite)