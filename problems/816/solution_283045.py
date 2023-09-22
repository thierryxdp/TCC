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
        del lista_inteiros[:n]
        lista_inteiros.sort()
    if n > max(lista_inteiros):
        lista_inteiros = []
    if (n < max(lista_inteiros) and n > min(lista_inteiros)) or n < min(lista_inteiros):
        lista_inteiros = max(lista_inteiros)
    return [lista_inteiros]