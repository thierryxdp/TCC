def maiores(lista, n):
    """
    	Recebe uma lista e um número <n>.
        Retorna uma nova lista com todos elementos da lista passada
        que são maiores que n.
        list, int --> list
    """
    novaLista = []
    for elemento in lista:
        if elemento > n:
            list.append(novaLista, elemento)
    list.sort(novaLista)
    return novaLista

def acima_da_media(lista):
    """
    	Recebe uma lista de notas e retorna uma lista com as notas que são
        que são maiores que a média.
        list --> list
    """
    media = sum(lista)/len(lista)
    notaMaiores = []
    for nota in lista:
        if nota > media:
            list.append(notaMaiores, nota)
    return notaMaiores