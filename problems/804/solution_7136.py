def filtra_pares(n1):
    tulpla = ()

    if n1[0] % 2 == 0:
        tulpla = tulpla  + (n1[0],)
    if n1[1] % 2 == 0:
        tulpla = tulpla  + (n1[1],)
    if n1[2] %2 == 0:
        tulpla = tulpla  + (n1[2],)
    if n1[3] % 2 == 0:
        tulpla = tulpla  + (n1[3],)

    return tulpla