def maiores(lista,n):
    """Dada uma lista1 de numeros, retorna outra lista contendo todos os numeros da lista original maiores que n e em ordem crescente
    list->list"""
    a=len(lista)
    list.sort(lista)
    if n in lista:
        atualizado=lista[(list.index(lista,n)+1):a]
        return atualizado
    elif n>=max(lista):
        return []
    if n not in lista and n<=min(lista):
        return lista