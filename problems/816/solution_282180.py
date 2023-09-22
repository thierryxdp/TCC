def maiores (lista,n):
    """retorna uma lista que contém todos os números da lista original
    maiores que n em ordem crescente"""
    list.sort(lista)
    if n > lista[:]:
        return []
    elif n < lista[:]:
        list.sort(lista)
        return lista