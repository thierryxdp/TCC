def eh_quadrada(mat):
    '''função que identifica se uma matriz é quadrada,levando em consideração que uma matriz vazia(sem nenhuma linha nem coluna) é considerada uma matriz quadrada; list (mat) -> bool'''
    b=True
    for i in mat:
        if b!=False:
            if len(i)==len(mat):    
                b=True
            else:
                b=False
    return b