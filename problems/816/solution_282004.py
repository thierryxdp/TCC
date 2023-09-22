def maiores(lista,n):
    '''Função que, dada uma lista de números inteiros e um número
    	inteiro, retorna outra lista de entrada com apenas os valores
        maiores que n em ordem crescente
        
        list, int -> list
        '''
    if n in lista:
        list.sort(lista)
        return lista[list.index(lista,n)+1:len(lista)]
    if n not in lista:
        lista = lista + [n]
        list.sort(lista)
        return lista[list.index(lista,n)+1:len(lista)]