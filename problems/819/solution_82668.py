def filtraMultiplos(lista,numero):
    '''função que recebe uma lista de números e um número e retorna outra contendo todos os
    números da lista original que forem divisíveis pelo número dado na entrada
    lista, float -> lista'''
    proximo = 0
    multiplos = []
    while proximo <len(lista):
        if lista[proximo]%numero == 0:
            multiplos = multiplos + [lista[proximo]]
        proximo = proximo + 1 
    return multiplos