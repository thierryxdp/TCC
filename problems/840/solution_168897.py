import math

def bolos (A=2, B=3, C=5):
    
    '''calcula quantos bolos podem ser feitos com os materiais entregues
       int, int, int, --> int'''
    
    farinha = A // 2
    
    ovos = B // 3
    
    leite= C //5
    
    return min(farinha, ovos, leite)