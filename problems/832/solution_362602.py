def eh_quadrada(M):
"""Recebe uma matriz, caso ela não tenha nenhuma linha nem
coluna ou tenha o mesmo número de linhas e colunas retorna
True. Caso contrário, retorna False
mat -> bool
"""
    if len(M) == 0 or len(M) == len(M[0]):
        return True
    else:
        return False