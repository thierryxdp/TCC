def maiores(ls, n):
    """
    maiores([1, 2, 10, 17, 19], 10) == [17, 19]
    maiores([1, 2, 10, 10, 10, 17, 19], 10) == [17, 19]
    
    maiores([10, 2, 1, 19, 17], 10) == [17, 19]
    """
    list.sort(ls)
    if n in ls:
        pos = list.index(ls, n)
        qtd = list.count(ls, n)
    	return ls[pos + qtd : ]
    return -1