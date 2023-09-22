def maiores(lista,n):
    '''
    Função que recebe uma lista de números inteiros e um
    número inteiro n e retorna outra lista que contenha 
    todos os números da lista original maiores que n.
    
    list, int -> list
    '''
    if n not in lista:
        lista.append(n)
    lista.sort()
    i=lista.index(n)
    c=lista.count(n)
    return lista[i+c:]