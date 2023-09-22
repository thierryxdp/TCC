def eh_quadrada(matriz):
  '''Essa função verifica se uma matriz é quadrada ou não,
  list->bool'''
  m1=matriz[0]
  m2=matriz[1]
  matriz=[m1,m2]
  if len(m1)<=2 and len(m2)<=2:
    return True
  else:
    return False