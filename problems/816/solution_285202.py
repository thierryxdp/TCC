def maiores(l1, n):
    '''
    	A função recebe uma lista numérica e um número inteiro n e retorna uma nova
        lista contendo todos os valores da lista anterior maiores que n, em ordem 
        crescente.
        n -> int
        l1 -> lista (contendo números)
    '''
    l1.append(n)
    l1.sort()
    an = l1.count(n)
    idn = l1.index(n)
    
    return l1[an + idn-1,]