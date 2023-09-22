def eh_quadrada(m):
    '''função que retorna True caso a matriz m inserida seja quadrada
    ou False caso ela não o seja
    list -> bool'''
    if m == [] or len(m) == len(m[0]):
        return True
    else:
        return False