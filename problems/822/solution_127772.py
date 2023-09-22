def repetidos(lstNum):    
    i= 0
    cont = 0
    while i <= (len(lstNum)-1):
        if lstNum[i] == lstNum[i-1]:
            cont += 1
        i += 1
        
        
    return cont