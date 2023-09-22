def eh_quadrada(x):
    '''Dada uma matrix X, identifica se ela é quadrada ou não.
    list -> bool'''
    a=0
    if x==[]:
        return True
    for i in range(len(x)):
        for j in range(len(x[i])):
            a=+1
    if i==j:
        return True
    else:
        return False