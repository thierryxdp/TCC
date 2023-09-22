def eh_quadrada(Matriz):
    '''retorna se matriz é quadrada ou não
    int->bool'''
    
    if Matriz==[]:
        return True
    if len(Matriz)==len(Matriz[0]):
        return True
    else:
        return False