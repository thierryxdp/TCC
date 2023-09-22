def maiores(L,n):
    """Retorna uma lista, que contenha todos os números da lista (L) maiores que n.
    lista,float-->lista)"""
    list.append(L,n)
    list.sort(L)
    x=list.index(L,n)
    return L[x+1:]

def media (lista):
    """Dada uma (lista) com as notas dos alunos de uma turma, retorna a média da turma e uma lista ordenada com as notas que ficaram acima da média.
    Lista-->float,lista"""
    M=sum(lista)/len(lista)
    Passou=maiores(lista,M+0.1)
    return M,Passou