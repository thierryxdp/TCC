def eh_quadrada(matrizada):
    ''' retorna se a matriz é quadrada;(list(list))->bool'''
    if len(matrizada)==0:
        return len(matrizada)==0
    if len(matrizada[0])==len(matrizada):
        return len(matrizada[0])==len(matrizada)
    else:
        return len(matrizada)==0