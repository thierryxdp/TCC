def acima_da_media(notas):
    """Função, que dada uma lista com as notas dos alunos, retoran uma lista ordenada com as notas que ficaram acima da média."""
    """list->list"""
    media = sum(notas)/len(notas)
    lista = notas + [media]
    list.sort(lista)
    lista_nova = lista[list.index(lista,media)+1:]
    return lista_nova