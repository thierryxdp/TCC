def eh_quadrada(x, y):
    '''Funcao recebe duas matrizes e retorna se elas sao quadradas ou nao'''
    resultado = True
    for i in x:
        if (resultado == False or len(i)!= len(x)):
            resultado = False
    return resultado