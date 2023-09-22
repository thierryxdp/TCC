def eh_quadrada(matrix):
    """função que retorna se uma matriz é quadrada ou não
    list->bool"""
    if matrix == [] or ['']:
        return true 
    else:
    	return len(matrix) == len(matrix[0])