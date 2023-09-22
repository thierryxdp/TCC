def maiores(lista,n):
    """Função que dada uma lista e um numero n retorna outra lista.List-->List """
    lista.append(n)
    lista.sort()
    pos = lista.index(n)
    return lista[pos+1:]
def acima_da_media(lista):
    """Função que retorna as notas que ficaram acima da média dos alunos de uma turma.List-->List"""
    media = (sum(lista)/len(lista))
    acima = maiores(lista,media)
    return media, acima