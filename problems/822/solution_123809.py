def repetidos(x):
    prox=1
    ant= prox - 1
    cont=0
    while prox<len(x):
        if x[prox] in x[ant]:
            count=count+1
        prox=prox + 1
    return count