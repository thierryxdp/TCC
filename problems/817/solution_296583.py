def maiores(listanumeros,n):
    """
    Função recebe uma lista de números inteiros(listanumeros) e um números inteiro n,
    retorna outra lista que contenha todos os números da lista original maiores do que n,
    ordenados em ordem crescente.
    lista, int -> lista
    """
    list.append(listanumeros,n)
    list.sort(listanumeros)
    vezes=list.count(listanumeros,n)
    posicao=list.index(listanumeros,n)+vezes
    return listanumeros[posicao:]

def acima_da_media(notas):
    """
    Função recebe uma lista com as notas dos alunos de uma turma e
    retorna uma lista ordenada com as notas que ficaram acima da média
    das notas.
    lista -> lista
    """
    media=sum(notas)/len(notas)
    return maiores(notas,media)