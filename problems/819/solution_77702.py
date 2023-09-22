filtraMultiplos([x],n):
    multiplos=()
    prox=0
    while prox<len(x):
        if x[prox]%n == 0:
            multiplos=multiplos +(x[prox],)
            prox=prox+1
    return multiplos