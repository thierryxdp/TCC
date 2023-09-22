def filtraMultiplos(lista_numeros,n):
    '''Função que recebe como entrada uma lista de números e um número n.
    Retorna outra lista com os elementos da lista original que forem divisíveis por n;
    list, int -> list'''
    multiplos = []
    proximo = 0
    while proximo <len(lista_numeros):
        if lista_numeros[proximo]%n == 0:
            multiplos = multiplos + [lista_numeros[proximo]]
        proximo = proximo + 1
    return multiplos