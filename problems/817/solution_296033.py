def acima_da_media(lista):
    '''dada uma lista com notas de alunos de uma turma, retorna
       uma nova lista com os alunos que ficaram acima da media da
       turma
       list -> list'''
    a=sum(lista)
    media=a/len(lista)
    list.append(lista,media)
    c=list.index(lista,media)
    return lista[(c+1):]