import math

def bolos (A=2, B=3, C=5):
    
    farinha = A // 2
    
    ovos = B // 3
    
    leite= C //5
    
    return min(farinha, ovos, leite)