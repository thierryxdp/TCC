def maiores(ls, n):
    """Recebe uma lista e um número inteiro 'n', e retorna uma lista com valores maiores que 'n' em ordem crescente
    testes: maiores([1,3,4], 1) == [3,4]
    maiores([5,4,1,2], 3) == [4,5]
    assinatura: list, int --> list
    """
    list.sort(ls)
    if n in ls:
        a = ls.index(n)
        b = ls.count(n)
        return ls[a+b+1]
    else:
        ls.append(n)
        list.sort(ls)
        c = ls.index(n)
        if ls[c] == max(ls):
            return []
        if ls[c] == min(ls):
            return ls[1:]
        else:
            return ls[c+1:]