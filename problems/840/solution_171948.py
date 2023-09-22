def bolos(farinha, ovo, leite):
    max_bolos = 0
    
    while farinha <= 0 or ovo <= 0 or leite <= 0:
        farinha -= 2
        ovo -= 3
        leite -= 5
        max_bolos += 1
        
    return max_bolos