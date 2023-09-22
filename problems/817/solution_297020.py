def maiores(lista, n):
    """Função que recebe uma lista de números inteiros e um
    número inteiro n. A função retorna outra lista que contenha
    todos os números da lista original maiores que número n, 
    ordenados em ordem crescente.
    list,int->list
    """
    nova_lista = lista + [n]
    list.sort(nova_lista)
    a = list.index(nova_lista, n)
    b = list.count(nova_lista, n)
    return nova_lista[ a + b : ]

def acima_da_media(lista):
    """Função que recebe uma lista com as notas dos alunos de uma
    turma e retorna uma lista, em ordem crescente, com as notas que 
    ficaram acima da média.
    list->list
    """
    calculo_media= sum(lista)/len(lista)
    return maiores (lista, calculo_media)