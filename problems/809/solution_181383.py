def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    nada = []
    listaum = lista1
    listadois = lista2
    lista_intercalada = [str(int(listaum[0]))+','+str(int(listadois[0]))+','+str(int(listaum[1]))+','+str(int(listadois[1]))+','+str(int(listaum[2]))+','+str(int(listadois[2]))]
    if len (lista1) and len(lista2) == 3:
        return lista_intercalada
    else:
        return nada