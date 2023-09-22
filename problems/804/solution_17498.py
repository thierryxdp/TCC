def filtra_pares (tupla):

    a,b,c,d = tupla 

    if tupla[a] % 2 == 0:
    
        tupla_nova (a,)

    if tupla[b] % 2 == 0:

        tupla_nova (a,b,)

    if tupla[c] %  2 == 0:

        tupla_nova (a,b,c,)

    if tupla[d] % 2 == 0:

        tupla_nova (a,b,c,d,)