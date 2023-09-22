def filtraMultiplos(lista,n):
    '''
    Função que recebe uma lista de números e um número
    e retorna outra lista contendo todos os elementos da lista 
    original que forem divisíveis por n
    '''
    contador = 0
    multiplos = []
    numero = lista[contador]
    
    while contador < len(lista):
        if numero%n == 0:
            multiplos = multiplos + (numero,)
        contador = contador + 1
    return multiplos