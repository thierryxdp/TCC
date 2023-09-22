def maiores(lista,n):
    '''Função que dada uma lista de numeros inteiros
    e um numero inteiro n, retorna outra lista que
    contenha todos os numeros da lista original 
    maiores que n, ordenados em ordem crescente
    '''
    lista.insert(0,n)
    return lista