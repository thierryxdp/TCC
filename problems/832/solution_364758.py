def eh_quadrada(M):
"""função que identifica se uma matriz é quadrada"""
nlin = len(M)
ncol = len (M[0])
   if len(M) == len (M[0]):
        return True
   else:
    return False