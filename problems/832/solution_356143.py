def eh_quadrada(Mat):
    '''recebe e retorna um argumento booleano se a matriz é quadrada ou não
    list -> bool'''
    
     if Mat == None:
        return True
    
    elif len(Mat) == len(Mat[0]):
        return True
    
    else:
        return False