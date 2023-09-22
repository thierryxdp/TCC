def eh_quadrada(mat):
    '''função que dada uma matriz retorna se ela é quadrada ou não; ???->bool'''
    lin = len(mat) or o
    col = len(mat[0]) or 0
    if lin ==col:
        return True
    elif lin==0 or col==0:
        return True
    else:
        return False