def maiores(ls, n):
    """Recebe uma  lista e um número inteiro 'n', e retorna uma lista de ordem crescente dos números da lista aneterior maiores que 'n'
    Testes: maiores([1,2,3,4,5], 2) == [3,4,5]
    maiores([5,4,3,2,1], 3) == [4, 5]
    assinatura: list, int --> list
    """
    list.sort(ls)
    if n in ls:
        a = list.index(ls, n)
        return ls[a+1:]
    if n not in ls:
        if n < ls[0]:
            return ls
        if n> ls[-1]:
            return []