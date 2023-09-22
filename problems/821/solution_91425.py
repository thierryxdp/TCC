def fatorial(n):
    '''it returns the factorial value of n
    int -> int'''
    factorial_value=1
    index=n
    while index>0:
        factorial_value=factorial_value*(index)
        index+=-1
    return factorial_value