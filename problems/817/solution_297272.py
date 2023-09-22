def acima_da_medias(listanotas):
    '''funcao que dada uma lista com as notas dos alunos da turma, retorna uma nova lista ordenada com as notas que ficaram acima da média;
       list->list'''
    media= sum(listanotas)/len(listanotas)
    list.insert(listanotas, 0, media)
    list.sort(listanotas)
    return listanotas[list.index(notas, media)+1:]