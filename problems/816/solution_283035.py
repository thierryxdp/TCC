def maiores(lista_inteiros,n):
    '''
    	Funcao recebe uma lista de numeros inteiros
        e um numero inteiro n e retorna outra lista 
        com todos os numeros da lista dada maiores que n, 
        em ordem crescente
        list -> list
        
    '''
    del lista_inteiros[:n]
    lista_inteiros.sort()

    return lista_inteiros