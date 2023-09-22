def media_matriz(mat):
    '''Função que dada uma matriz de inteiros não vazia, retorna
    a média de todos os númeroos da matriz (com exatamente duas
    casas decimais de precisão);
       mat --> float'''
    import numpy
    a = len(mat)
    b = len(mat[0])
    c = numpy.sum(mat)
    d = c/(a*b)
    e = round(d,2)
    return e