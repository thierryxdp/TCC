def soma_h(x):
    acum=0
    for i in range(1,x+1):
        H=1/i
        acum += H
    return round(acum,2)