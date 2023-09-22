def fatorial(n):
  ''' 
  Recebe um int 
  Retorna um int
  '''
  if n == 0:
        return 1
  else:
    return n*fatorial(n-1)