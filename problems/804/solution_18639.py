def filtra_pares (tupla):
	""" Esta função retorna uma tupla que elimina dados impares
	tuple -> int, int ,int ,int """
    a,b,c,d = tupla
    tupla_nova = ()

    if a % 2 == 0:
    
     tupla_nova = tupla_nova + (a,)

    if b % 2 == 0:

      tupla_nova = tupla_nova + (b,)

    if c %  2 == 0:

      tupla_nova = tupla_nova + (c,)

    if d % 2 == 0:

       tupla_nova = tupla_nova + (d,)


    return tupla_nova