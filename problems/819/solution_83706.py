def filtraMultiplos(lista,numero):
    filtro = ()
    i = 0
    while i < len(lista):
        if lista[i]%numerob== 0:
            filtro = filtro + (lista[i],)
        i = i + 1
    return filtro