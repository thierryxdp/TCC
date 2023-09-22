def eh_quadrada(matrizquadrada):
    '''A função retorna True se a matriz for quadrada e Falsa se não for
    list->bool'''
    if len(matrizquadrada)>0:
        if len(matrizquadrada)==len(matrizquadrada[0]):
            return True
        else:
            return False
        else:
            return True