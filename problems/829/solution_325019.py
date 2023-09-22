def soma_h(inteiro):    
    H = 1
    for numero in list(range(inteiro)):
        if numero > 0:
        	H += 1/numero
    return round(H,2)