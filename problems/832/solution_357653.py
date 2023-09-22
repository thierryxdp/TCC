def eh_quadrada(x):
    '''Função booleana que identifica se uma matriz é quadrada;
       Entrada: lista
       Saída: bool'''
    if x==[]:
        return True
    if len(x[0])==len(x):
        return True
    else:
        return False