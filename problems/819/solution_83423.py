def filtraMultiplos(lista,n):
    '''Função que recebe uma lista de numeros e um número e retorna outra lista contendo todos os elementos da lista original que forem divisíveis por n;
       list,int->list'''
    multiplos = []
    proximo = 0
    while proximo<len(lista):
        if lista[proximo]/n==int:
            multiplos = multiplos + [lista[proximo],]
        proximo = proximo + 1
    return multiplos