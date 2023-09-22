# Matriz Quadrada
def eh_quadrada(matriz):
    '''Essa função recebe uma matriz em forma de lista de listas e retorna
    se ela é do tipo quadrada ou não;
    LIST -> BOOL'''
    if len(matriz) == 0:
        return True
    else:
        if len(matriz) == len(matriz[0]):
            return True
        else:
            if len(matriz[0]) == 0:
                return 'None'
            else:
                return False