def filtra_pares (tupla):

    a,b,c,d = tupla 
	tupla_nova = ()

    if a % 2 == 0:
    
        tupla_nova + (a,)

    if b % 2 == 0:

        tupla_nova + (a,b,)

    if c %  2 == 0:

        tupla_nova + (a,b,c,)

    if d % 2 == 0:

        tupla_nova + (a,b,c,d,)

	return tupla_nova