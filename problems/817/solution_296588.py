def acima_da_media(lista):
    """ dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas acima da média 5
    list -> list"""
    list.sort(lista)
    indice = list.find (lista, 5)
    lista = lista[indice+1:]
    return lista