def acima_da_media(notas):
    '''funcao que recebe como parametro uma lista com notas dos alunos de uma turma e retorne outra lista com as notas acima da media da lista de entrada de
       forma ordenada(crescente)
       list->list'''
    media= sum(notas)/len(notas)
    list.insert(notas,0,media)
    list.sort(notas)
    a=list.index(notas,media)
    if list.count(notas,media)==1:
        return notas[a+1:]
    else:
        return notas[a+2:]