def bolos(farinha, ovo, leite):
    max_bolos = 0
    
    while farinha >= 2 and ovo >= 3 and leite >= 5:
        farinha -= 2
        ovo -= 3
        leite -= 5
        max_bolos += 1
        
    return max_bolos