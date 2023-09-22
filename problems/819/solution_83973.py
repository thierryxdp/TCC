def filtraMultiplos(lista, n):
    '''Recebe uma lista de numeros (lista), e um
    número inteiro (n). Retorna outra lista contendo
    todos os elementos da lista original que forem
    divisíveis por n
    
    list, int -> list
    '''
    
    multiplos = []
    contador = 0
    
    while contador < len(lista):
        if lista[contador] % n and n == 0:
            multiplos.insert(contador, lista[contador])
            contador = contador + 1
    return multiplos