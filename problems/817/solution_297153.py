def maiores(lista_numero,n):
    """Dado uma lista de números inteiros e um número n, retorna a lista
    em ordem crescente à partir dos números maiores que n:
    list,int-->list"""
    lista_numero=lista_numero+[n]
    lista_numero.sort()
    del lista_numero[0:lista_numero.index(n)]
    lista_numero.remove(n)
    return lista_numero

def acima_da_media(notas_da_turma):
    """Dado uma lista de notas de uma turma de alunos, retorna as notas que
    ficaram acima da média:
    list-->list"""
    if len(notas_da_turma)==1:
        return []
    else:
        n=sum(notas_da_turma)/len(notas_da_turma)
        notas_da_turma.remove(n)
        notas_da_turma=maiores(notas_da_turma,n)
    return notas_da_turma