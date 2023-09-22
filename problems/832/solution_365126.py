def eh_quadrada(matrix):
    '''Function that, given a matrix as parameter,
    return True, if it`s squared, or False, if it
    isn`t.
    List --> Bool.'''
    if len(matrix) > 0:
        return len(matrix) == len(matrix[0])
	return True