def eh_quadrada(matriz):
    '''função booleana que  identificar se uma matriz é quadrada.
    Observação: uma matriz vazia (sem nenhuma linha nem coluna) é considerada quadrada.
    list->bool'''
    if matriz==[]:
        return True
    linha=len(matriz)
    coluna=len(matriz[0])
    if linha==coluna:
        return True
    else:
        return False