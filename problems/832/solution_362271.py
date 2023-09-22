def eh_quadrada(mat):
    '''identifica se uma matriz é quadrada'''

    lin=len(mat)
    col=len(mat[0])
    num=0

    for i in range(lin):
      if lin == col or lin and col==[]:  
       num=num+1
       return True

    for i in range(lin):
     if lin != col:
      return False