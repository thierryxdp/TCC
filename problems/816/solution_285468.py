def maiores(l_numeros,n):
    '''Recebe uma lista e um número inteiro e retorna outra
    lista que contem todos os números da lista original
    maiores que n, ordenados me ordem crescente.
    list, int -> list'''
    nova_lista = []
	menor = min(l_numeros)
    numeros = tuple(l_numeros)
    if n > menor:
        nova_lista += [numeros]
        return nova_lista