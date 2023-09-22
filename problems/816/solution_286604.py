def maiores(ls, n):
    """Recebe uma lista de 4 elementos e um número inteiro 'n', retornando uma lista em ordem crescente contendo os números maiores do que n
    Testes: maiores([1,2,3,4], 1) == [2,3,4]
    maiores([4,3,2,1], 1) == [2,3,4]
    assinatura: list, int --> list
    """
    list.sort(ls)
    ret = []
    if ls[0] > n:
        ret.append(ls[0])
    if ls[1] > n:
        ret.append(ls[1])
    if ls[2] > n:
        ret.append(ls[2])
    if ls[3] > n:
        ret.append(ls[3])
    return ret