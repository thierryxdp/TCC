def filtraMultiplos(l,n):
    '''função que dada uma lista não vazia de inteiros e um número 
    inteiro, retorna uma lista com os inteiros da lista original que são
    divisíveis pelo número escolhido.
    list, int -> list'''
    multiplos = []
    proximo = 0
    while proximo < len(l):
        if l[proximo]%n == 0:
            multiplos.append(l[proximo])
        proximo = proximo +1
    return multiplos