def filtra_pares(t):
  '''Função recebe uma tupla com quatro valores inteiros, verifica, um por um,
  se são pares, e retorna uma nova tupla apenas com os valores pares, na ordem
  em que foram informados.
    tuple -> tuple'''
  x = ()
  if t[0] % 2 == 0:
    x += (t[0],)
  if t[1] % 2 == 0:
    x += (t[1],)
  if t[2] % 2 == 0:
    x += (t[2],)
  if t[3] % 2 == 0:
    x += (t[3],)
  
  return x