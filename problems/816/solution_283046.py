def maiores(lista_inteiros,n):
    '''
    	Funcao recebe uma lista de numeros inteiros
        e um numero inteiro n e retorna outra lista 
        com todos os numeros da lista dada maiores que n, 
        em ordem crescente
        list -> list
        
    '''
    if n in lista_inteiros:
        lista_inteiros.sort()
        del lista_inteiros[:list.index(lista_inteiros,n)+1]
        lista_inteiros.sort()
        return lista_inteiros
    else:
        list.extend(lista_inteiros,[n,])
        lista_inteiros.sort()
        del lista_inteiros[:list.index(lista_inteiros,n)+1]
        lista_inteiros.sort()
        return lista_inteiros