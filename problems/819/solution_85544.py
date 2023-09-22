def filtraMultiplos(lista,n):
    """
    Função que recebe uma lista de números e um número
    e retorna outra lista contendo todos os elementos da lista 
    original que forem divisíveis por n
    """
    contador = 0
    multiplos = []
    
    while contador < len(lista):
        if lista[contador]%n == 0:
            multiplos = multiplos + [lista[contador],]
        contador = contador + 1
    return multiplos