def filtra_pares(n1, n2, n3, n4):
    tulpla = ()
    if n1 % 2 == 0:
        tulpla = tulpla  + (n1,)
    if n2 % 2 == 0:
        tulpla = tulpla  + (n2,)
    if n3 %2 == 0:
        tulpla = tulpla  + (n3,)
    if n4 % 2 == 0:
        tulpla = tulpla  + (n4,)

    return tulpla