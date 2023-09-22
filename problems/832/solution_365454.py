def eh_quadrada(mat):

    index=0
    
    if len(mat)== 0:
        return True
    
    for x in mat:
        if len(x) == len(mat):
            index= index +1
            
    if index == len(mat):
        return True
    else:
        return False