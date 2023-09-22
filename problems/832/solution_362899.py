def eh_quadrada(mat):
    lin = 0 
    col = 0 
    for i in range(len(mat)):
    	for j in range(len(mat)):
        	col = col + 1
            lin = lin + 1
        	if lin== col:
            	return False
    for i not in range(len(mat)):
        for j not in range(len(mat)):
            return True