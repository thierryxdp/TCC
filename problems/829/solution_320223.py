def soma_h(inteiro):
    H = 1
    
    for dividendo in range(1, inteiro + 1):
        if (dividendo <= inteiro):
            H += 1 / dividendo
    return H.round(2)