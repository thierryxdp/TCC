def acima_da_media(notas):
    '''funcao que dada uma lista com as notas dos alunos da turma retorna uma lista ordenada com as notas que ficaram acima da media
    list->list'''
    if media not in notas:
    media=sum(notas)/len(notas)
    list.append(notas,media)
    list.sort(notas)
    i=list.index(notas,media)
    else:
        return notas[i+1:]