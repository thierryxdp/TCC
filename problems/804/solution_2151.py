def filtragem(tupla):

    tupla_nova = ()

    if tupla[0] % 2 == 0:
        tupla_nova = tupla_nova + (tupla[0],)
    if tupla[1] % 2 == 0:
        tupla_nova = tupla_nova + (tupla[1],)
    if tupla[2] % 2 == 0:
        tupla_nova = tupla_nova + (tupla[2],)
    if tupla[3] % 2 == 0:
        tupla_nova = tupla_nova + (tupla[3],)

    return tupla_nova