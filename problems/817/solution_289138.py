def acima_da_media(lista):
    '''dada uma lista com notas dos alunos de uma turma, retorna uma lista ordenada com as notas que ficaram acima da media
    lista -> lista'''
    a = sum(lista)
    b = len(lista)
    media = a//b
    t = media
    if media in lista:
        return lista[t+1:]
    else:
        listaNova = lista + [t]
        list.sort(listaNova)
        if listaNova[-1] <= t:
            return []
        else:
            x = list.index(listaNova, t)
            return listaNova[t+1:]