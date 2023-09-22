def acima_da_media(lis,x):
    """Função que dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas que ficaram acima da média"""
    """list->list"""
    if x in lis:
        list.insert(lis,0,x)
        list.sort(lis)
        y=lis[z+2:]
        z=list.index(lis,x)
        return y
    else:
        list.insert(lis,0,x)
        list.sort(lis)
        z=list.index(lis,x)
        y=lis[z+1:]
        return y
    return maiores (lis,sum(lis)/len(lis))