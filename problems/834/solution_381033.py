def media_matriz(matrix):
    '''Function that receives a matrix of intergers as 
    entry parameter and returns the avarage of all its 
    numbers with 2 decimal places.
    List --> Float.'''
    somatory = 0
    numbOfElements = len(matrix)*len(matrix[0])
    for line in matrix:
        for number in line:
            somatory += number
    avarage = somatory/numbOfElements
    return round(avarage,2)