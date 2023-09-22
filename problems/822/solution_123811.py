def repetidos(x):
    prox=1
    count=0
    while prox<len(x):
        if x[prox] == x[prox - 1]:
            count=count+1
        prox=prox + 1
    return count