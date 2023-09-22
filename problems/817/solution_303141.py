def acima_da_media(lista):
    """funçao recebe lista e retorna lista ordenada
    list--> list"""
    media = int(sum(lista) / len(lista))

def maiores(lista, n):
        """funçao recebe lista e n ́umero inteiro e retorna
        lista com elementos da entrada a partir do n ́umero inteiro
        list, int--> list"""
        if n in lista:
            list.sort(lista)
            lista1 = lista[list.index(lista, n) + 1:]
            return lista1
        else:
            lista.insert(-1, n)
            list.sort(lista)
            lista1 = lista[list.index(lista, n) + 1:]
            return lista1
        return maiores(lista, media)