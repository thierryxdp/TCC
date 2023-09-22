def eh_quadrada(m):
    '''Função booleana para identificar se uma matriz é quadrada.
       parâmetro de entrada:list
       valor de retorno:bool'''
    if len(m)==0:
        return None
    if len(m)==len(m[0]):
        return True 
    else:
        return False