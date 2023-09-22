def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    nada = []
    listaum = lista1
    listadois = lista2
    lista_intercalada = [listaum[0], listadois[0], listaum[1], listadois[1], listaum[2], listadois[2]]
    if len (lista1) and len(lista2) == 3:
         return lista_intercalada
    else:
        return nada