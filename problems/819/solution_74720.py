def filtraMultiplos(lista,n):
    '''função que filtra os múltiplos de um número n e retornar outra lista contendo todos os elementos da lista original que forem divisíveis por n.
    entrada: list, int
    saída:  list'''
    acumulador = [ ] 
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]%n == 0:
            acumulador = list.append(acumulador,lista[proximo])
        proximo = proximo + 1
    return len(lista)