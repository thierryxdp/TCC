def repetidos(sequencia):
    i = 0
    acum = 0
    while i < len(sequencia):
        if sequencia[i] == sequencia [i-1]:
             acum = acum  +1
        i = i+1
    return acum