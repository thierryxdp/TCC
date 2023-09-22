def filtraMultiplos(lista,numero):
    filtro = ()
    if lista[0]%numero==0:
        filtro = filtro + (lista[0],)
    if lista[1]%numero==0:
        filtro = filtro + (lista[1],)
    if lista[2]%numero==0:
        filtro = filtro + (lista[2],)
    if lista[3]%numero==0:
        filtro = filtro + (lista[3],)
    if lista[4]%numero==0:
        filtro = filtro + (lista[4],)
    if lista[5]%numero==0:
        filtro = filtro + (lista[5],)
        return filtro