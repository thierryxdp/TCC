def qtd_divisores(n):
    """  """
    for i in range(1,n//2+1):
        if n%i==0:
            n=i
    return n