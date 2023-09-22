def filtraMultiplos(listan, n):
    """Funcao que retorne outra lista contendo todos os elementos da lista original que forem divisíveis por n.
    list, int -> list"""
    indice += 1
    novaLista = []
    while indice < listan:
        if listan[indice] % n ==0:
            list.append(novaLista, listan[indice])
    	            return novaLista