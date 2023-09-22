def soma_h (n):
    H = [1]
    i=0
    for x in H:
        if H[i]>=1/n:
            i+=1
            H+=[[1]/[i]]
            
    return H