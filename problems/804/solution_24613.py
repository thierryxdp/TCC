def filtra_pares(elementos):
    pares = ()
    if (int(elementos[0])%2)==0:
        pares += (elementos[0],)
    if (int(elementos[1])%2)==0:
        pares += (elementos[1],)
    if (int(elementos[2])%2)==0:
        pares += (elementos[2],)
    if (int(elementos[3])%2)==0:
        pares += (elementos[3],)
    return pares