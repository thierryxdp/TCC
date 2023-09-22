def acima_da_media(lista_notas):
    '''função que recebe uma lista que contém a nota dos alunos
    de uma turma (lista_notas) e que retorna uma nova lista ordenada
    com as notas dos alunos que ficaram acima da média
    lista->lista'''
    media = int(sum(lista_notas)/len(lista_notas))
    list.sort(lista_notas)
    list.append(lista_notas, media)
    list.sort(lista_notas)
    p = list.index(lista_notas,media) + 1
    return lista_notas[p:]