def fatorial(x):
    """calcula o fatorial de um valor dado
    int -> int
    """
    if x == 0:
        return 1
    else:
        produto = 1
        while(num>1):
            produto*= x
            num -= 1
            return produto