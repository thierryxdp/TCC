def eh_quadrada(Mat):
    '''recebe e retorna um argumento booleano se a matriz é quadrada ou não
    list -> bool'''
    
    if len(Mat) == len(Mat[0]) or Mat == [[]] :
        return True
    
    else:
        return False