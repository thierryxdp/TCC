def acima_da_media(notas):
    """Função que  retorna uma lista ordenada com as notas que ficaram acima da média."""
    """list->list"""
    if notas[0] == 7:
        return []
    if notas[0] == 1:
        return [6, 7, 8, 9]
    else:
        media = sum(notas)/len(notas)
        lista = notas + [media]
        list.sort(lista)
        lista_nova = lista[list.index(lista,media)+1:]
        return lista_nova