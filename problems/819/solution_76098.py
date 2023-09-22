def filtraMultiplos (lista,n):
    "Função que filtra os multiplos de um numero que deve retornar uma lista com todos os elementos da lista original divisíveis por n"
    indice = 0 
    lista1 = []
    while indice < len (lista):
        if lista[indice] % n == 0:
            lista1 = lista1 + [lista[indice]]
        indice = indice + 1
    return lista2