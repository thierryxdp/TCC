def eh_quadrada(A):
    '''funcao que, dada uma matriz A, verifica se ela e ou nao quadrada;
    matriz -> bool'''
    nLinhas = len(A)
    nColunas = len(A[0])
    if nLinhas == nColunas:
        return True
    else:
        return False