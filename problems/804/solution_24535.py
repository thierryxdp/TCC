def filtra_pares (tupla):
    '''Função que voltrá os números pares dada a sequência com 4 núemros'''
    tupla_nova=()
    if len(tupla)==4:
        if tupla[0]%2==0:
            tupla_nova +=(tupla[0],)
        if tupla[1]%2==0:
            tupla_nova +=(tupla[1],)
        if tupla[2]%2==0:
            tupla_nova +=(tupla[2],)
        if tupla[3]%2==0:
            tupla_nova +=(tupla[3],)
    return tupla_nova