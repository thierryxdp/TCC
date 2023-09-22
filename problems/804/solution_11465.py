def filtra_pares(tupla):
    "Quatro elementos inteiros da tupla."
    tupla final = ()
    if tupla[0] % 2 == 0:
        tupla final += (tupla[0],)
    if tupla[1] % 2 == 0:
        tupla final += (tupla[1],)
    if tupla[2] % 2 == 0:
        tupla final += (tupla[2],)
    if tupla[3] % 2 == 0:
        tupla final += (tupla[3],)
    return tupla final