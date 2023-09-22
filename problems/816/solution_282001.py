def maiores(lista,n):
    '''Função que, dada uma lista de números inteiros e um número
    	inteiro, retorna outra lista de entrada com apenas os valores
        maiores que n em ordem decrescente
        
        list, int -> list
        '''
    list.sort(lista)
    x = lista[n:len(lista)]
    return x