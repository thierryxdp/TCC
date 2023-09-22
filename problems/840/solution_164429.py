#Questao 3
import math

def bolos(n_xicaras, n_ovos, n_colher):
    '''Calcula a quantidade de bolos que é possivel
    fazer com a quantidade de ingredientes dados
    '''
    return math.floor(min(n_xicaras/2, n_ovos/3, n_colher/5))