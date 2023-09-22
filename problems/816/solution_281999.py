def maiores(numeros:list[int],n:int)->list[int]:
    '''Retorna uma lista com todos os elementos
    da lista que são maiores que n.'''
    numerosCopia = numeros.copy()
    numerosCopia.append(n)
    numerosCopia.sort()
    posicaoN = numerosCopia.index(n)
    numerosMaiores = numerosCopia[posicaoN+1:]
    
    return numerosMaiores