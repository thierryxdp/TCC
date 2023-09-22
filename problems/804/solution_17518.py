def filtra_pares (tupla):

    a,b,c,d = tupla 
	tupla_nova = ()

    if a % 2 == 0:
    
        tupla_nova + (a,)

    if b % 2 == 0:

        tupla_nova + (b,)

    if c %  2 == 0:

        tupla_nova + (c,)

    if d % 2 == 0:

        tupla_nova + (d,)

	return tupla_nova