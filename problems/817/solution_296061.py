def acima_da_media(lista):
    '''dada uma lista com notas de alunos de uma turma, retorna
       uma nova lista com os alunos que ficaram acima da media da
       turma
       list -> list'''
    a=sum(lista)
    media=a/len(lista)
    list.append(lista,media)
    list.sort(lista)
    c=list.index(lista,media)
    b=lista[(c+1):]
    if (media==5.0) and (5.0 in b):
        list.remove(lista,5.0)
    if len(lista)>2:
        return b
    else:
        return []