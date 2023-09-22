def eh_quadrada(mat):
    lin = 0 
    col = 0 
    for i in range(len(mat)):
        lin = lin + 1
    for j in range(len(mat)):
        col = col + 1
        
        if lin == col:
            return False