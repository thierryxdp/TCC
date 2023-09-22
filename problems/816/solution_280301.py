def maiores(numeros: List[int], n: int):
    '''Funcao que calcula e retorna os numeros maiores que n.
    int->int'''
    for i in numeros:
        if i > n:
            return list(i)