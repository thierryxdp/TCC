def eh_quadrada(mat):
    '''função que dada uma matriz retorna se ela é quadrada ou não; list->bool'''
    vazia = []
    if mat == vazia:
        return True
    elif mat != vazia:
        lin=len(mat)
        col=len(mat[0])
        if lin==col:
            return True
        else:
            return False