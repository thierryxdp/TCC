def qtd_divisores(n):
    """wkdfejslkfnkes"""
    
    num = []
    
    for x in range(1, n+1):
        if n % x == 0:
            num = num + [x,]
    return len(num)