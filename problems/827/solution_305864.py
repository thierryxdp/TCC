def qtd_divisores(x):
    '''Função que recebe um número e conta quantos divisores ele tem.
    entrada da função: int
    saída da função: int'''
    result = 0
    for i in range(1, x//2+1):
        prod = 1
        for c in range (i, 0, -1):
            prod = prod % c
        result += prod    
        
    return result