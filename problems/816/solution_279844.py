def maiores(lista, n):
    '''Função que recebe uma lista de int's e um int(n);
e retorna outra lista, contendo os números da lista original maiores que o int dado(n)
list, int-> list'''
    if n not in lista:
        lista.append(n)
        lista.sort( )
        i = lista.index(n)
        sublista = lista[i+1:]
        repeticao = sublista.count(n)
        return sublista[repeticao:]