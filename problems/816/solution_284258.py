def maiores(numeros: list[int],n: int,estritamente: bool = False) -> list[int]:
    '''Retorna uma lista com todos os numeros da lista
       de entrada que são maiores que n'''
    numerosCopia = numeros.copy()
    numerosCopia.append(n)
    numerosCopia.sort()
    posicaoN = numerosCopia.index(n)
    numerosMaiores = numerosCopia[posicaoN+1:]
    return numerosMaiores