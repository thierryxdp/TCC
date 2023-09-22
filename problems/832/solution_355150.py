def eh_quadrada(m):
    '''Função booleana que retorna se a matriz m é quadrada
    list[list] -> bool'''
    if len(m)==len(m[0]):
        return True
    if len(m[0])==0:
        return True
    else:
        return False