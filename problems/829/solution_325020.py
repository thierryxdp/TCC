def soma_h(inteiro):    
    for numero in [list(range(inteiro)),inteiro]:
        if numero > 0:
        	H += 1/numero
    return round(H,2)