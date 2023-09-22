def filtraMultiplos(lista,n):
    """Dada uma lista de números e um número 'n', a função retorna outra lista
    contendo todos os elementos da lista original que são divisíveis por n;
    list,int -> list"""
    multiplos = []
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]%n == 0:
            multiplos = multiplos + [lista[proximo],]
        proximo = proximo +1
    return multiplos