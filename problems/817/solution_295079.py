def acima_da_media(lista_notas,media):
    '''A partir de uma lista com a nota dos alunos retorna
    uma lista com as notas dos alunos que ficaram acima da
    media.
    list -> list'''
    list.append(lista_notas,media)
    list.sort(lista_notas)
    list.reverse(lista_notas)
    lista = lista_notas[:list.index(lista_notas,n)]
    list.reverse(lista)
    return lista