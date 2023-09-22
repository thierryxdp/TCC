def qtd_divisores(n):
    """llkfdjsklfnsdk"""
    
    div = []
    
    for x in range (1, n+1):
        if n % x == 0:
            div += 1
    return len(div)