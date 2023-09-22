def maiores(lista,n):
    '''Função que dada uma lista com números inteiros e um
    número inteiro n retorne uma outra lista, dessa vez com 
    apenas os números maiores que n da lista original
    list, int --> list.'''
    if n not in lista:
        lista.append(n)
        lista.sort()
        a = lista.index(n)
        lista_numeros = lista[a+1:]
        rep = lista_numeros.count(n)
        return lista_numeros[rep:]