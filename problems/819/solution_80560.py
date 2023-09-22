def filtraMultiplos(lista,n):
    '''funcao que dada uma lista com numeros e um numero, retorna outra lista contendo todos os elementos da lista original que forem divisiveis por n'''
    '''list -> list'''
    lista2 = []
    proximo = 0
    while proximo <len(lista):
        if lista[proximo]%n == 0:
            lista2 = lista2 + [lista[proximo]]
            proximo = proximo + 1
            return lista 2