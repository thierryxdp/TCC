def filtra_pares(tupla):
    tuplaO=()
    if tupla[0] % 2 == 0:
        tuplaO = tuplaO + (tupla[0], )
    if tupla [1] % 2 == 0:
        tuplaO = tuplaO + (tupla[1], )
    if tupla [2] % 2 == 0:
        tuplaO = tuplaO + (tupla[2], )
    if tupla [3] % 2 == 0:
        tuplaO = tuplaO + (tupla[3], )
        return tuplaO