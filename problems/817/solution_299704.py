def acima_da_media(lista_notas:list)->list:
    """Dada uma lista com notas dos alunos, retorna uma lista ordenada com notas que ficaram acima da média."""
    if len(lista_notas) > 1:
        media = sum(lista_notas)/len(lista_notas)
        lista_notas.append(media)
        lista_notas.sort()
        num = lista_notas.index(media)
        rept = lista_notas.count(media)
        del lista_notas[0:num+rept]
        return lista_notas
    else:
        return []