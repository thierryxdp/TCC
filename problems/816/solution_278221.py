def maiores(lista, n):
    '''Função que recebe uma lista de inteiros e um número inteiro n e retorna outra lista
    com todos os números da lista original maiores que n; list, int -> list'''
    
    lista2 = []
    cont = 0
    while cont < len(lista):
        if lista[cont] > n:
            list.append(lista2, lista[cont])
        cont += 1

    return lista2