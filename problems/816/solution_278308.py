def maiores(Lista,N):
    """ Função que dada uma lista de números inteiros e um número inteiro N, retorna outra lista, que contenha
    todos os números da lista original maiores que N """
    Lista.append(N)
    Lista.sort()
    index = Lista.index(N)
    return Lista[index + 1 :]