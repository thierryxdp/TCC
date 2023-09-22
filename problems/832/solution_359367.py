def eh_quadrada(x):
    '''Dada uma matrix X, identifica se ela é quadrada ou não.
    list -> bool'''
    a=0
    b=0
    for i in range(len(x)):
        a=a+1
        for j in range(x[i]):
            b=b+1
    if a==b:
        return True
    else:
        return False