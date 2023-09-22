def maiores(Lista,N):
    """ Função que dada uma lista de números inteiros e um número inteiro N, retorna outra lista, que contenha
    todos os números da lista original maiores que N. """
    Lista.append(N)
    Lista.sort()
    index = Lista.index(N)
    return Lista[index + 1 :]

def acima_da_media(Lista):
    """ Função que dada uma lista com as notas dos alunos de uma turma, retorna a média da turma e uma lista
    ordenada com as notas que ficaram acima da média. """
    media=sum(Lista)/len(Lista)
    maiores=maiores(Lista,media)
    if media in maiores:
        maiores.remove(media)
    return maiores