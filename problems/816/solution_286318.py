def maiores(ls, n):
    """
    maiores([1, 2, 10, 17, 19], 10) == [17, 19]
    maiores([10, 2, 1, 19, 17], 10) == [17, 19]
    """
    list.sort(ls)
    pos = list.index(ls, n)
    return ls[pos + 1 : ]