def repetidos(x):
  """função que retorna o numero de vezes que o elemento da lista
     é igual ao numero anterior
     ent-list
     saida:int
   """
  resposta= 0
  t= 0
  while t<(len(x)-1):
    if x[t] == x[t+1]:
        resposta += 1
    t += 1
  return resposta