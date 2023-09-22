def maiores(inteiros, n):
    
    ''' Função que, dada uma lista de números
        inteiros e um número inteiro (n), retorna
        uma lista contendo os números da lista
        original que são maiores que n, em 
        ordem crescente.
        list, int -> list '''
    
    inteiros.sort()
    
    
    if n in inteiros:
        inteiros = inteiros[inteiros.index(n) + 1:]
    
    if n not in inteiros:
        inteiros.append(n)
        inteiros.sort()
        inteiros = inteiros[inteiros.index(n) + 1:]
        
    return inteiros