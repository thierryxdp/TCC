def filtraMultiplos (lista,n):
    """Função que filtra os múltiplos de um número 'n' e deve retornar uma lista contendo os elementos da lista original que forem divisíveis por ' n'"""
    """lista -> lista"""
    lista2 = []
    proximo = 0
    while proximo < len(lista):
        if lista [proximo]%n == 0:
            lista2 = lista2 + [lista[proximo]]
        proximo = proximo + 1
    return lista2