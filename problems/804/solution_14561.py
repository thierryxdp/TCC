#Start your python function heredef  filtra_pares(n)

    if n[0] % 2 == 0:

        tupla_final = (n[0],)

    if n[1] % 2 == 0:

        tupla_final += (n[1],)

    if n[2] % 2 ==  0:

        tupla_final += (n[2],)

    if n[3] % 2 ==  0:

        tupla_final += (n[3],)

    return tupla_final