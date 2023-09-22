def soma_h(n):
    sequencia=0
    for c in range(1,n+1):
        H=1/c
        sequencia+=H
    return round(sequencia,2)