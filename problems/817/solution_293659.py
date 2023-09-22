def acima_da_media(lista):
    s=sum(lista)
    f=len(lista)
    n=(s/f)+0.001
    list.extend(lista,[n])
    list.sort(lista)
    lista1=list.index(lista,n)
    return lista[(lista1+1):1000]
'''recebe uma lista com as notas de alunos e retorna outra lista com as 
notas maiores que a media da turma dispostas de maneira ordenada,list->list'''