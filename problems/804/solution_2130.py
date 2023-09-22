def filtra_pares (a,b,c,d):
    #(Tupla de 4 int)-> (tupla com int par)
    if (a%2) and (b%2) == 0:
        return a,b
    if (a%2) and (c%2) == 0:
        return a,c
    if (a%2) and (d%2) == 0:
        return a,d
    if (b%2) and (c%2) == 0:
        return b,c
    if (b%2) and (d%2) == 0:
        return b,d
    if (c%2) and (d%2) == 0:
        return c,d
    else:
        return 'Nenhum deles são pares'