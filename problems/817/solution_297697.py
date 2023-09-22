def acima_da_media (lista):
    """dada uma lista com as notas dos alunos de uma turma, retorna uma lista com as notas que ficaram acima da media;
    list->list"""
    x=sum(lista,1)
    y=len(lista)
    n=(x/y)
    d=[n]
    list.extend(lista,d)
    list.sort(lista)
    nova=list.index(lista,n)
    new=lista[nova+1:]
    return new