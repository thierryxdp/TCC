def maiores(lista: list, n: int) -> list:
    """Essa função, dada uma lista de números inteiros e um
	 número inteiro n, retorna uma nova lista contendo todos os
	 números da lista original maiores que n"""
    i = 0
    lista_maiores = []
    
    while i < len(lista):
        if lista[i] > n:
            lista_maiores = lista_maiores + [lista[i],]
        i = i+ 1
    
    return sorted(lista_maiores)