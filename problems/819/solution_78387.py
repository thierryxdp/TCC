def filtraMultiplos(lista,n):
    """Função que dada uma lista e um número inteiro n, retorna outra lista com todos os elementos da lista original divisíveis por n
lista, int -> lista"""

    multiplos = ()
    indice = 0
    
    while indice <len(lista):
        if lista[indice]%n == 0:
            multiplos = multiplos + (lista[indice],)
        indice = indice + 1
    return multiplos