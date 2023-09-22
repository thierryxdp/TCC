def soma_h(inteiro):    
    H = 1
    for numero in list(range(inteiro)):
        H += 1/numero
    return round(H,2)