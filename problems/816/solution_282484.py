def maiores(lista,n):
    '''Dados uma lista de números inteiros e um número inteiro,
    retorna uma nova lista com os valores da lista original
    que forem maiores que (n) 
    list, int -> list '''
    a=([i for i in lista if i > n])
    return sorted(a)