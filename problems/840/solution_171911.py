def bolos (A,B,C):
    
    if A>=2 and B>= 3 and C>=5:
        farinha = A//2
        ovos = B//3
        leite = C//5
        
        ingredientes = min(farinha, ovos, leite)
        
        if ingredientes>=1:
            bolos = ingredientes
    
    else:
        bolos = 0
    
    return bolos