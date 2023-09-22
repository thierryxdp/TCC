def maiores(lista,n):
    '''Função que, dada uma lista de números inteiros e um número
    	inteiro, retorna outra lista de entrada com apenas os valores
        maiores que n em ordem decrescente
        
        list, int -> list
        '''
    if n in lista:
        list.sort(lista)
        list.reverse(lista)
        return lista[0:list.index(n)]
    if n not in lista:
        lista = lista + [n]
        list.sort(lista)
        list.reverse(lista)
        return lista[0:list.index(n)]