filtraMultiplos(lista,n):
    multiplos=()
    prox=0
    while prox<len(lista):
        if lista[prox]%n == 0:
            multiplos=multiplos +(lista[prox],)
            prox=prox+1
    return multiplos