def filtra_pares (a,b,c,d):
    #(Tupla de 4 int)-> (tupla com int par)
    if (a%2) and (b%2) == 0:
        return a,b
    elif (a%2) and (c%2) == 0:
        return a,c
    elif (a%2) and (d%2) == 0:
        return a,d
    elif (b%2) and (c%2) == 0:
        return b,c
    elif (b%2) and (d%2) == 0:
        return b,d
    elif (c%2) and (d%2) == 0:
        return c,d
    else:
        return 'Nenhum deles são pares'