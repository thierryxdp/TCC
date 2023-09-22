def maiores(lista,n):
    """Função que dada uma lista de números inteiros(lista) e um número inteiro (n),
    retorna outra lista, que contenha todos os números da lista original maiores que 'n';
    list, int ->list"""

    if n not in lista:
        list.append(lista,n)

    list.sort(lista)
    indice = list.index(lista,n)

    n_maiores = lista[indice+1:]

    return n_maiores

def acima_da_media(lista):
    """Função que dada uma lista com as notas dos alunos de uma turma, retorna uma uma lista
    ordenada com as notas que ficaram acima da média; list -> list"""

    media = sum(lista)/len(lista)

    return maiores(lista,media)