def maiores(lis,x):
    if x in lis:
        list.insert(lis,0,x)
        list.sort(lis)
        z=list.index(lis,x)
        y=lis[z+2:]
        return y
    else:
        list.insert(lis,0,x)
        list.sort(lis)
        z=list.index(lis,x)
        y=lis[z+1:]
        return y
def acima_da_media(lis):
    """Função que dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas que ficaram acima da média"""
    """list->list"""
    return maiores (lis,sum(lis)/len(lis))