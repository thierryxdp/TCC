def maiores(lis,x):
    """Função que dada uma lista de números inteiros e um número inteiro x, retorna outra lista, que contenha todos os números da lista origina maiores que x, ordenadoos em ordem crescente"""
    """list,int->list"""
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