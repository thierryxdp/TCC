def eh_quadrada(mat):
    b=True
    for i in mat:
        if b!=False:
            if len(i)==len(mat):    
                b=True
            else:
                b=False
    return b