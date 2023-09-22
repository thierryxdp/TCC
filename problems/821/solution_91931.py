def fatorial(x):
    """calcula o fatorial de um valor dado
    int -> int
    """
    if x == 0:
        return 1
    else:
        produto = 1
        while(x>1):
            produto*= x
            x -= 1
            return produto