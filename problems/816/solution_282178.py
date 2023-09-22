def maiores (lista,n):
    """retorna uma lista que contém todos os números da lista original
    maiores que n em ordem crescente"""
    if n > lista[0:-1]:
        return []