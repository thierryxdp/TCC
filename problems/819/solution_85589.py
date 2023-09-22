def filtraMultiplos(lista_numeros, n):
    """função que recebe como entrada uma lista de números e um número(n), e retorna uma outra lista contendo todos os elementos da lista original divisíveis por n
    string -> string"""
    Multiplos = []
    indice = 0
    while indice < len(lista_numeros):
        if lista_numeros[indice]%n==0:
            Multiplos = (Multiplos,[lista[indice]])
            indice += 1
    return Multiplos