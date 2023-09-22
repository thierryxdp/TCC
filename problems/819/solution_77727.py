def filtraMultiplos(lista_numeros,n):
    """A função recebe como entrada uma lista de números
    (lista_numeros) e um número (n), e retornará outra 
    lista contendo todos os elementos da lista original 
    que forem divisíveis por n. Isto é: todos os múltiplos
    de n.
    Entrada: List
    Saída: Int"""
    
    i=0
    numeros=()
    while i<len(lista_numeros):
        if lista_numeros[i]%n == 0:
            numeros = numeros + (lista_numeros[i],)
        i = i + 1
    return list(numeros)